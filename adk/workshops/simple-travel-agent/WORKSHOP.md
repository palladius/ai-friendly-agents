# Workshop: Building a Simple Travel Agent

Welcome to the ADK workshop! In this session, we will build a simplified travel agent step-by-step.

## Prerequisites

Ensure you have `uv` installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Step 1: Basic Agent

Let's start by creating a basic agent that can have a conversation.

Create a file named `agent.py`:

```python
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import asyncio

async def main():
    # 1. Define the Agent
    travel_agent = LlmAgent(
        name="simple_travel_agent",
        model="gemini-2.5-flash",
        instruction="You are a helpful travel assistant. You can help users plan their trips.",
    )

    # 2. Set up Session and Runner
    session_service = InMemorySessionService()
    runner = Runner(agent=travel_agent, session_service=session_service)

    # 3. Run the interactive loop
    print("Travel Agent: Hello! Where would you like to go?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        events = runner.run_async(
            user_id="workshop_user",
            session_id="session_01",
            new_message=types.Content(role='user', parts=[types.Part(text=user_input)])
        )

        async for event in events:
            if event.is_final_response():
                print(f"Travel Agent: {event.content.parts[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
```

Run it:
```bash
uv run agent.py
```

Try asking it: "Book a hotel in Milan for today and tomorrow."
It will likely fail to know specific dates.

## Step 2: Add the `now()` tool

The agent doesn't know what "today" is. Let's give it a tool.

Add this function to `agent.py`:

```python
from datetime import datetime

def now() -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

Update the agent definition to include the tool:

```python
    travel_agent = LlmAgent(
        name="simple_travel_agent",
        model="gemini-2.5-flash",
        instruction="You are a helpful travel assistant. Use the `now` tool to get the current date when needed.",
        tools=[now]
    )
```

Run it again and ask the same question. It should now know the date!

## Step 3: Add Google Search

It still can't find real hotels. Let's add Google Search.

Import it:
```python
from google.adk.tools import google_search
```

Add it to the tools list:
```python
        tools=[now, google_search]
```

Run it again. Now it can find real hotels!

## Step 4: Integrate MCP (Model Context Protocol)

To get more specific data (like Airbnb listings), we can use MCP.
*(Instructions for setting up MCP client would go here)*

## Milestone 1 Complete!

You now have a functional travel agent that knows the time and can search the web.