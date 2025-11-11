import logging
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from pydantic import PrivateAttr

class FlightAgent(LlmAgent):
    _logger: logging.Logger = PrivateAttr()

    def __init__(self, name: str, model: str, log_file: str = None):
        # Construct the absolute path to flight_planner_server.py
        # Assuming google-flights-mcp is a sibling directory to workshop-travel-agent
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'google-flights-mcp', 'src'))
        flight_mcp_path = os.path.join(project_root, "flight_planner_server.py")

        toolset = MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='python',
                    args=[flight_mcp_path],
                ),
            )
        )
        super().__init__(
            name=name,
            model=model,
            instruction="You are a flight agent. Your main task is to find flights by using the tools provided by the flight search MCP.",
            description="A flight agent that finds flights by calling a flight search MCP.",
            tools=[toolset]
        )
        self._logger = logging.getLogger(self.name)
        if log_file is None:
            log_file = f"log/{self.name}.log"
        handler = logging.FileHandler(log_file, mode="a")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)
        self._logger.info(f"Initializing FlightAgent with name: {self.name}")
