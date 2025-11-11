import datetime
from google.adk.agents import Agent
from google.adk.tools import tool
from google.adk.tools import google_search

@tool
def get_now() -> str:
    """Returns the current date and time."""
    date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"status": "success", "current_time": date_now}

root_agent = Agent(
    name="travel_search",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant. You can search the web for the latest travel information and have access to the current time.",
    tools=[get_now, google_search],
)