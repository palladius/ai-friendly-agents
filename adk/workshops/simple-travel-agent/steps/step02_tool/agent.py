import datetime
from google.adk.agents import Agent

# =========================================
# STEP 3: Uncomment the following line to import Google Search
# =========================================
# from google.adk.tools import google_search
# =========================================

def now() -> dict:
    """Returns the current date and time."""
    return {
        "status": "success",
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

root_agent = Agent(
    name="travel_tool",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant. You have access to the current time.",
    tools=[
        now,
        # =========================================
        # STEP 3: Uncomment to register Google Search
        # =========================================
        # google_search,
        # =========================================
    ],
)
