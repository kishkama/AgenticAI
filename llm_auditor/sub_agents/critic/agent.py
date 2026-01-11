from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse
from google.adk.tools import google_search
from . import  prompt

def _render_reference(
        callback_context: CallbackContext,
        llm_response: LlmResponse,
) -> LlmResponse:
    """
    Appends grounding references to the response
    """
    del callback_context
    # GroundingChunkWeb uses 'uri' not 'url'
    if getattr(llm_response, "grounding_metadata", None):
        refs = []
        for chunk in llm_response.grounding_metadata.grounding_chunks or []:
            web = getattr(chunk, "web", None)
            if web:
                title = getattr(web, "title", "")
                uri = getattr(web, "uri", "")
                if uri:
                    refs.append(f"- {title}: {uri}" if title else f"- {uri}")
        if refs:
            llm_response.text = (llm_response.text or "") + "\n\nSources:\n" + "\n".join(refs)
    return llm_response

critic_agent = Agent(
    model = "gemini-2.5-flash",
    name = "critic_agent",
    instruction=prompt.CRITIC_PROMPT,
    tools=[google_search],
    after_model_callback=_render_reference
)