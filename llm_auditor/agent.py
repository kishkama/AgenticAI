from google.adk.agents import SequentialAgent
from .sub_agents.critic import critic_agent
from .sub_agents.reviser import reviser_agent

llm_auditor = SequentialAgent(
    name="llm_auditor",
    description=(
        'evaluate the llm generated answers, verify actual accuracy using web search,'
        'and refines the response to ensure alignment with the real world'
    ),
    sub_agents=[critic_agent,reviser_agent]
)
root_agent = llm_auditor