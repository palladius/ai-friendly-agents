from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="travel_search",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant. You can search the web for the latest travel information.",
    tools=[google_search],
)
