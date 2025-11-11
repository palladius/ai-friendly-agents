import asyncio
import argparse
import yaml
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from src.hotel_agent import HotelAgent
from src.data_classes import HotelSearchQuery

async def main():
    """Main function to run the hotel agent in isolation."""
    parser = argparse.ArgumentParser(description="Run the Hotel Agent in isolation.")
    parser.add_argument(
        "--query",
        default="etc/sample-hotel-query.yaml",
        help="Path to the hotel search query file."
    )
    args = parser.parse_args()

    with open(args.query, "r") as f:
        query_data = yaml.safe_load(f)
    
    query = HotelSearchQuery(**query_data)

    agent = HotelAgent(name="TestHotelAgent", model="gemini-2.5-flash")
    
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name="hotel_agent_test",
        user_id="test_user",
        session_id="test_session"
    )
    
    runner = Runner(
        agent=agent,
        app_name="hotel_agent_test",
        session_service=session_service
    )

    prompt = f"Please find a hotel with the following details: {query.model_dump_json(indent=2)}"
    print(f"Sending prompt to agent:\n{prompt}\n")

    content = types.Content(role='user', parts=[types.Part(text=prompt)])
    events = runner.run_async(
        user_id="test_user",
        session_id="test_session",
        new_message=content
    )

    async for event in events:
        if event.is_final_response():
            response_text = event.content.parts[0].text
            print(f"\nFinal response from agent:\n{response_text}")

if __name__ == "__main__":
    asyncio.run(main())

