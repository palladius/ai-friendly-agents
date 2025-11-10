import asyncio
import argparse
import os
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from src.concierge_agent import ConciergeAgent
from src.config import load_config, load_hotel_data

async def main():
    """Main function to run the concierge agent."""
    parser = argparse.ArgumentParser(description="Run the Concierge Agent.")
    parser.add_argument(
        "-f", "--file",
        default="etc/sample-family.yaml",
        help="Path to the family configuration file."
    )
    args = parser.parse_args()

    config_path = os.path.abspath(args.file)
    family_config = load_config(config_path)
    hotel_data = load_hotel_data("etc/sample-hotel.yaml")

    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="travel_agent",
        user_id="user123",
        session_id="session456"
    )

    concierge = ConciergeAgent(name="Androsthenes", model="gemini-2.5-flash", family_config=family_config, hotel_data=hotel_data)
    runner = Runner(
        agent=concierge,
        app_name="travel_agent",
        session_service=session_service
    )

    print("Welcome to the Travel Agent! How can I help you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "quit"]:
            break

        content = types.Content(role='user', parts=[types.Part(text=user_input)])
        events = runner.run_async(
            user_id="user123",
            session_id="session456",
            new_message=content
        )

        async for event in events:
            if event.is_final_response():
                print(f"Androsthenes: {event.content.parts[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
