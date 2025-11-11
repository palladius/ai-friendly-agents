import unittest
import asyncio
import os
import tempfile
import yaml
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from datetime import datetime

from src.concierge_agent import ConciergeAgent
from src.config import load_config, load_flight_data, load_hotel_data
from src.data_classes import Family

class TestConciergeAgent(unittest.TestCase):
    def setUp(self):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        config_path = os.path.join(project_root, "etc", "sample-family.yaml")
        self.family_config = load_config(config_path)

    def test_greet_user_with_config(self):
        """Tests that the concierge agent greets the user and uses config details."""
        async def run_test():
            session_service = InMemorySessionService()
            session = await session_service.create_session(
                app_name="test_app",
                user_id="test_user",
                session_id="test_session"
            )

            concierge = ConciergeAgent(name="TestConcierge", model="gemini-2.5-flash", family_config=self.family_config)
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
            self.assertIn("Riccardo", final_response)

        asyncio.run(run_test())

    def test_propose_default_travel_plan(self):
        """Tests that the agent proposes the default travel plan."""
        async def run_test():
            session_service = InMemorySessionService()
            await session_service.create_session(app_name="test_app", user_id="test_user", session_id="test_session")

            concierge = ConciergeAgent(name="TestConcierge", model="gemini-2.5-flash", family_config=self.family_config)
            runner = Runner(agent=concierge, app_name="test_app", session_service=session_service)

            content = types.Content(role='user', parts=[types.Part(text="I want to go on a trip")])
            events = runner.run_async(user_id="test_user", session_id="test_session", new_message=content)

            final_response = ""
            async for event in events:
                if event.is_final_response():
                    final_response = event.content.parts[0].text
            
            self.assertIn("Milan", final_response)
            self.assertIn("Sal", final_response)
            self.assertIn("Capo Verde", final_response)

        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()
