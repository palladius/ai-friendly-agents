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
from src.config import load_config
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
            self.assertIn(self.family_config.Family[0].Surname, final_response)
            self.assertIn(self.family_config.TravelProps.TravellerType, final_response)
            self.assertIn(datetime.now().strftime("%Y-%m-%d"), final_response) # Check for current date

        asyncio.run(run_test())

    def test_greet_user_with_file_argument(self):
        """Tests that the agent can be run with a file argument."""
        async def run_test():
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".yaml") as temp_file:
                temp_config = {
                    "Family": [{"Name": "Test", "Surname": "McTestFace", "Role": "Tester", "DOB": "2023-01-01", "PassPort": "T12345678", "Interests": ["Testing"]}],
                    "Address": {"Street": "123 Test St", "City": "Testville", "Country": "Testland", "ZipCode": "12345"},
                    "TravelProps": {"TravellerType": "Adventurous", "PreferredAirlines": [], "HotelPreferences": [], "DietaryRestrictions": [], "SpecialNeeds": []},
                    "Budget": {"TotalBudget": "1000 USD", "BudgetFlexibility": "strict", "Days": 1, "MealPerPerson": "10 USD", "AccommodationPerNight": "100 USD"}
                }
                yaml.dump(temp_config, temp_file)
                temp_file_path = temp_file.name

            family_config = load_config(temp_file_path)
            
            session_service = InMemorySessionService()
            await session_service.create_session(app_name="test_app", user_id="test_user", session_id="test_session")

            concierge = ConciergeAgent(name="TestConcierge", model="gemini-2.5-flash", family_config=family_config)
            runner = Runner(agent=concierge, app_name="test_app", session_service=session_service)

            content = types.Content(role='user', parts=[types.Part(text="Hello")])
            events = runner.run_async(user_id="test_user", session_id="test_session", new_message=content)

            final_response = ""
            async for event in events:
                if event.is_final_response():
                    final_response = event.content.parts[0].text
            
            self.assertIn("McTestFace", final_response)

            os.remove(temp_file_path)

        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()
