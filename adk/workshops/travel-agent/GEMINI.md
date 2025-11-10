
We want to create an app using ADK.

## The app

The app is described under `THE_APP.md`.

App should be testable in isolation, without running the agents, and each agent should have some tests.

We'll use a `.env` for ENV variables (such as `GEMINI_API_KEY`) which you CANNOT write, EVER!

Use python + `uvx` to minimize virtualenv issues.

## Our interaction

Make sure to read ADK documentation under `travel-agent/rag/adk-python/llms-full.txt`
and use its context to build ADK.
