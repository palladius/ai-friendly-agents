"""This is the solution_1 agent code for the simple travel agent workshop."""

from google.adk.agents import Agent
# from google.adk.tools import google_search # (This will be needed in STEP 3)

# =========================================
# STEP 2: Uncomment the following lines to add a tool
# =========================================
# import datetime
#
# def get_now() -> str:
#     """Returns the current date and time."""
#     date_now = ...
#     return {"status": "success", "current_time": date_now}
# =========================================

root_agent = Agent(
    name="travel_basic",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant. You can help with general travel advice based on your knowledge.",
    # =========================================
    # STEP 2: Uncomment to register the tool
    # =========================================
    # tools=[get_now],
    # =========================================
)
