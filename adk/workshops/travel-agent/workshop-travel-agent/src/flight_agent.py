import logging
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams
from pydantic import PrivateAttr

class FlightAgent(LlmAgent):
    _logger: logging.Logger = PrivateAttr()

    def __init__(self, name: str, model: str, mcp_url: str = "http://localhost:8000", log_file: str = None):
        toolset = MCPToolset(
            connection_params=SseConnectionParams(url=mcp_url)
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
        handler = logging.FileHandler(log_file, mode="w")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)
        self._logger.info(f"Initializing FlightAgent with name: {self.name}")
