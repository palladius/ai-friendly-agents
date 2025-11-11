import unittest
import asyncio
from unittest.mock import patch, MagicMock
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from src.hotel_agent import HotelAgent
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

class MockStdioConnectionParams(StdioConnectionParams):
    model_config = {"arbitrary_types_allowed": True}
    def __init__(self, server_params):
        self.server_params = server_params

class TestHotelAgent(unittest.TestCase):
    @patch("src.hotel_agent.StdioConnectionParams", new=MockStdioConnectionParams)
    def test_search_hotels(self):
        """Tests that the hotel agent can find hotels in a given destination."""
        async def run_test():
            session_service = InMemorySessionService()
            await session_service.create_session(
                app_name="test_app",
                user_id="test_user",
                session_id="test_session"
            )

            agent = HotelAgent(name="TestHotelAgent", model="gemini-2.5-flash")
            runner = Runner(
                agent=agent,
                app_name="test_app",
                session_service=session_service
            )

            content = types.Content(role='user', parts=[types.Part(text="Find hotels in Sal, Capo Verde")])
            events = runner.run_async(
                user_id="test_user",
                session_id="test_session",
                new_message=content
            )

            final_response = None
            async for event in events:
                if event.is_final_response():
                    final_response = event.content.parts[0].text
                    break
            
            self.assertIsNotNone(final_response)
            self.assertIn("Hilton Sal", final_response)

        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()
