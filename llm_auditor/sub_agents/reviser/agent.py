from google.adk import Agent

reviser_agent = Agent(
    model = "gemini-2.5-flash",
    name = "critic_agent",
    instruction="",
    #TODO : add callback
)