# Workshop: Building a Simple Travel Agent

Welcome to the ADK workshop! In this session, we will build a simple travel agent step-by-step.

*Curiosity*: This workshop was built by Riccardo Carlesso with help from Gemini CLI. If you're curious, you can find how i did it by
looking at the `GEMINI.md` and `WORKSHOP_PLAN.md` in this folder.

**Solutions**. Note: the code is all contained under `steps/`. If you don't want to cheat, you can just read there. For the purpose of this
Lab, this is ok. We're not here to learn how to write good ADK code, but how to set up yuour environment to get GOOD code automatically written
under your direction. (1) Installing the software, (2) configuring / getting it to work, and (3) entering the Golden Feedback Loop is what we
really want you to learn here.

## Prerequisites (Installation)

For this tutorial, you need to install:
1. `python` and `uv` (best package manager for Python). Ensure you have `uv` installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **[Gemini CLI](https://github.com/google-gemini/gemini-cli)**. For gemini CLI, find installation instructions here: https://github.com/google-gemini/gemini-cli .
   1. Note this requires having `npm` or `npx` installed.
   2. On Mac, you can use `brew`
   3. On Windows, you can use `chocolatey` or just download the executable from https://nodejs.org/en/download



## Step 0: set up your work environment

```bash
$ mkdir -p mysolution/
$ touch mysolution/__init__.py mysolution/agent.py
```



## Step 1: Basic Agent


Let's start by creating a basic agent that can have a conversation.

Create a file named `mysolution/__init__.py`:

```python
from .agent import root_agent
```

As simple as that! This allows ADK to know where your code is: in `agent.py`.

Create a file named `mysolution/agent.py`:

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="travel_basic",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant. You can help with general travel advice based on your knowledge.",
)
```

### Testing the agent

This is true for all the steps. ADK allows you to test your agent in two ways: CLI and Web.
* **CLI** is best for quick and automated tests
* **Web** is the best to visually see what's happening, use microphone (!), and troubleshooting.

Run it from bash (CLI):
```bash
uv run mysolution/agent.py
```

![Gemini doesnt even know what day is it](image.png)

Try asking it: *"Book a hotel in Milan for today and tomorrow"*

It will likely fail to know specific dates. We need to teach it to know the date!

For web, you can do this:

```bash
uv web # runs all agents under this folder. You want to point it to  "mysolution/" subfolder
```

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
        name="..",
        model="..",
        instruction="..",
        # This is the only line you want to add.
        tools=[now]
    )
```

Run it again and ask the same question. It should now know the date, and be vague about hotels!

Try asking it: *"Book a hotel in Milan for today and tomorrow"*


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
