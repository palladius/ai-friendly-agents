from __future__ import annotations
import datetime
from google.adk.agents import Agent
from google.adk.tools import FunctionTool, google_search
from google.adk.tools.agent_tool import AgentTool

def now() -> dict:
    """Returns the current date and time."""
    return {
        "status": "success",
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Create a simple agent whose only job is to search.
search_agent = Agent(
    name="SearchAgent",
    model="gemini-2.5-flash",
    tools=[google_search],
)

# Wrap the search_agent in an AgentTool.
search_tool = AgentTool(agent=search_agent)

# Create the time tool from our simple Python function.
time_tool = FunctionTool(func=now)

# The root agent can now use both the AgentTool and the FunctionTool.
root_agent = Agent(
    name="RootAgent",
    model="gemini-2.5-flash",
    tools=[
        search_tool,
        time_tool,
    ],
    instruction="""
You are a helpful travel agent.
You have two tools:
1. A search engine to find real-time information.
2. A tool to get the current time.

- If the user asks for the time, use the `now` tool.
- For any other questions requiring up-to-date information, use the search tool.
""",
)