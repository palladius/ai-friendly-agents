import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search

def now() -> dict:
    """Returns the current date and time."""
    return {
        "status": "success",
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

root_agent = Agent(
    name="travel_search",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant. You can search the web for the latest travel information.",
    # Note: gemini-2.5-flash currently does not support mixing Google Search (Grounding)
    # with other Function Calling tools. So we replace get_now with google_search here.
    tools=[google_search],
)