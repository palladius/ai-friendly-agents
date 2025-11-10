import unittest
import asyncio
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from src.concierge_agent import ConciergeAgent

class TestConciergeAgent(unittest.TestCase):
    def test_greet_user(self):
        """Tests that the concierge agent can greet the user."""
        async def run_test():
            session_service = InMemorySessionService()
            session = await session_service.create_session(
                app_name="test_app",
                user_id="test_user",
                session_id="test_session"
            )

            concierge = ConciergeAgent(name="TestConcierge", model="gemini-2.5-flash")
            runner = Runner(
                agent=concierge,
                app_name="test_app",
                session_service=session_service
            )

            content = types.Content(role='user', parts=[types.Part(text="Hello")])
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
            self.assertIn("Hello", final_response)

        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()
