from google.adk.agents import Agent

# =========================================
# STEP 2: Uncomment the following lines to add a tool
# =========================================
# from google.adk.tools import tool
# import datetime
#
# @tool
# def get_now() -> str:
#     """Returns the current date and time."""
#     date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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