import asyncio
import argparse
import os
import logging
from datetime import datetime
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from src.concierge_agent import ConciergeAgent
from src.config import load_config

async def main():
    """Main function to run the concierge agent."""
    # Suppress verbose logging from libraries
    logging.basicConfig(level=logging.WARNING)
    logging.getLogger('google.genai').setLevel(logging.CRITICAL)
    logging.getLogger('google.adk').setLevel(logging.CRITICAL)
    logging.getLogger('asyncio').setLevel(logging.CRITICAL)

    parser = argparse.ArgumentParser(description="Run the Concierge Agent.")
    parser.add_argument(
        "-f", "--file",
        default="etc/sample-family.yaml",
        help="Path to the family configuration file."
    )
    parser.add_argument(
        "-q", "--query",
        help="Initial query to send to the Concierge Agent."
    )
    args = parser.parse_args()

    config_path = os.path.abspath(args.file)
    family_config = load_config(config_path)

    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="travel_agent",
        user_id="user123",
        session_id="session456"
    )

    concierge = ConciergeAgent(name="Androsthenes", model="gemini-2.5-flash", family_config=family_config)
    runner = Runner(
        agent=concierge,
        app_name="travel_agent",
        session_service=session_service
    )

    print("Welcome to the Travel Agent! How can I help you today?")
    
    if args.query:
        user_input = args.query
        print(f"> {user_input}")
        # Process the query and then exit
        content = types.Content(role='user', parts=[types.Part(text=user_input)])
        events = runner.run_async(
            user_id="user123",
            session_id="session456",
            new_message=content
        )

        async for event in events:
            if event.is_final_response():
                if event.content and event.content.parts:
                    print(f"Androsthenes: {event.content.parts[0].text}")
                else:
                    print("Androsthenes: I encountered an issue and cannot provide a response.")
    else:
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
                    if event.content and event.content.parts:
                        print(f"Androsthenes: {event.content.parts[0].text}")
                    else:
                        print("Androsthenes: I encountered an issue and cannot provide a response.")

if __name__ == "__main__":
    asyncio.run(main())
