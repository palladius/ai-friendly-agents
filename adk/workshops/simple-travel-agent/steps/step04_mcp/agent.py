import datetime
from google.adk.agents import Agent
# from google.adk.tools import google_search # Cannot be mixed with Function Tools in gemini-2.5-flash
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

def get_now() -> str:
    """Returns the current date and time."""
    date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"status": "success", "current_time": date_now}

# Configure the Airbnb MCP Toolset
airbnb_mcp = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=["-y", "@openbnb/mcp-server-airbnb"],
        ),
    )
)

root_agent = Agent(
    name="travel_mcp",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant. You can find accommodation using Airbnb, and have access to the current time.",
    tools=[get_now, airbnb_mcp],
)
