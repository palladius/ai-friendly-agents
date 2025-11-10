import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from src.concierge_agent import ConciergeAgent

async def main():
    """Main function to run the concierge agent."""
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="travel_agent",
        user_id="user123",
        session_id="session456"
    )

    concierge = ConciergeAgent(name="Androsthenes", model="gemini-2.5-flash")
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
