from google.adk.agents import Agent

# =========================================
# STEP 2: Uncomment the following lines to add a tool
# =========================================
# from google.adk.tools import tool
# import datetime
#
# @tool
# def get_current_time() -> str:
#     """Returns the current date and time."""
#     return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# =========================================

root_agent = Agent(
    name="simple_travel_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant.",
    # =========================================
    # STEP 2: Uncomment to register the tool
    # =========================================
    # tools=[get_current_time],
    # =========================================
)
