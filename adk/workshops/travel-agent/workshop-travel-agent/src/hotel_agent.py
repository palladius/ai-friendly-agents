import logging
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from pydantic import PrivateAttr

class HotelAgent(LlmAgent):
    _logger: logging.Logger = PrivateAttr()

    def __init__(self, name: str, model: str, log_file: str = None):
        toolset = MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                    args=["-y", "@openbnb/mcp-server-airbnb"],
                ),
            )
        )
        super().__init__(
            name=name,
            model=model,
            instruction="You are a hotel agent. Your main task is to find hotels by using the tools provided by the Airbnb MCP.",
            description="A hotel agent that finds hotels by calling the Airbnb MCP.",
            tools=[toolset]
        )
        self._logger = logging.getLogger(self.name)
        if log_file is None:
            log_file = f"log/{self.name}.log"
        handler = logging.FileHandler(log_file, mode="w")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)
        self._logger.info(f"Initializing HotelAgent with name: {self.name}")
