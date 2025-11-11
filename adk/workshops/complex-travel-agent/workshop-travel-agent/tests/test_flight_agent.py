import unittest
import asyncio
from unittest.mock import patch, MagicMock
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from src.flight_agent import FlightAgent

class TestFlightAgent(unittest.TestCase):
    @patch("google.adk.tools.mcp_tool.mcp_session_manager.MCPSessionManager._generate_session_key", lambda x, y: "test_session_key")
    @patch("src.flight_agent.StdioConnectionParams")
    def test_search_flights(self, mock_stdio_connection_params):
        """Tests that the flight agent can find flights to a given destination."""
        async def run_test():
            mock_stdio_connection_params.return_value = MagicMock()
            session_service = InMemorySessionService()
            await session_service.create_session(
                app_name="test_app",
                user_id="test_user",
                session_id="test_session"
            )

            agent = FlightAgent(name="TestFlightAgent", model="gemini-2.5-flash")
            runner = Runner(
                agent=agent,
                app_name="test_app",
                session_service=session_service
            )

            content = types.Content(role='user', parts=[types.Part(text="Find flights to Sal, Capo Verde")])
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
            self.assertIn("TAP Air Portugal", final_response)

        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()
