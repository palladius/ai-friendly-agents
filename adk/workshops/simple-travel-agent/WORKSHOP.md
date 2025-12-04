<!--
Note: thjis workshop was first done in:

* 2025-11-18: Milan by Riccardo and Giancluca Menconi
* 2025-12-04: Geneve by Riccardo and Daniel S and Charley E.

<img src="slides-adk-cli.svg" width="30%" align="right">

-->

<img src="events/adk-worskhop-qr-code.png" width="40%" align="right">

[Workshop self-link](https://github.com/palladius/ai-friendly-agents/blob/main/adk/workshops/simple-travel-agent/WORKSHOP.md): https://goo.gle/adk-cli-workshop

**_Event Information_**

- 🇨🇭 **Geneva** 📅 Dec 2025 **[Workshop instructions](events/20251204-geneva.md)**. Slides: https://goo.gle/adk-cli-geneve-slides
- 🇮🇹 **Milan 📅 Nov 2025**: [obsolete](events/202511-milan.md)

# Workshop: Building a Simple Travel Agent

Welcome to the ADK workshop! In this session, we will build a simple travel agent step-by-step.

_Curiosity_: This workshop was built by Riccardo Carlesso with help from Gemini CLI. If you're curious, you can find how i did it by
looking at the `GEMINI.md` and `WORKSHOP_PLAN.md` in this folder.

<img src="adk_web_select_steps.png" width="30%" align="right">

**Solutions**. Note: the code is all contained under `steps/`. If you don't want to cheat, you can just read there. For the purpose of this
Lab, this is ok. We're not here to learn how to write good ADK code, but how to set up yuour environment to get GOOD code automatically written
under your direction. (1) Installing the software, (2) configuring / getting it to work, and (3) entering the Golden Feedback Loop is what we
really want you to learn here. You can also test them all at the same time via `just web-4steps`!

## Prerequisites (Installation)

For this tutorial, you need to install:

1. `python` and `uv` (best package manager for [Python](https://www.python.org/downloads/)). This is needed for **ADK**. Ensure you have [uv](https://github.com/astral-sh/uv) installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **[Gemini CLI](https://github.com/google-gemini/gemini-cli)**. For gemini CLI, find installation instructions here: https://github.com/google-gemini/gemini-cli .
   1. Note this requires having `npm` or `npx` installed.
   2. On Mac, you can use `brew` as per [official docs](https://github.com/google-gemini/gemini-cli).
   3. On Windows, you can use `chocolatey` or just download the executable from https://nodejs.org/en/download

For step 4, you'll also need `npx` installed. Both `npm` and `npx` should come naturally as part of Gemini CLI. If not, ask Gemini CLI to help you here.

Optionally, you might also want to install [just](https://github.com/casey/just), it's a 21st century `Makefile` if you like makefiles. Also here: ask Gemini CLI to help you install this, he could do it for you!

3. **Authentication**. You need either a Google Cloud Project with Vertex AI enabled, or a [Google AI Studio API Key](https://aistudio.google.com/api-keys).
   - **Option A (Recommended for Workshop):** Export your API Key:
     ```bash
     export GOOGLE_API_KEY="your-api-key"
     ```
   - **Option B (Vertex AI):** Authenticate with gcloud:
     ```bash
     gcloud auth application-default login
     export VERTEX_PROJECT_ID="your-project-id"
     export VERTEX_LOCATION="us-central1"
     ```

## Step 0: set up your work environment

You're going to create your OWN solution under `mysolution/` so let's create the folder and the two files we need.

This is the moment where you can open your IDE (Visual Studio Code, IntelliJ, RubyMine, ..) and open the folder.

```bash
# 1. Find an empty directory, and download this repo.
git clone https://github.com/palladius/ai-friendly-agents/
cd ai-friendly-agents/adk/workshops/simple-travel-agent/

# 2. Create your solution empty skeleton
mkdir -p mysolution/
touch mysolution/__init__.py mysolution/agent.py

# 4. Installs ADK and MCP via `uv` by reading pyproject.toml
uv sync

# 4. Call Gemini CLI
gemini  # This runs Gemini CLI under the simple-travel-agent/ folder.
# Login with your GMail account.
```

`uv sync` is not strictly required, but if it fails, you know you need to fix your [Python](https://www.python.org/downloads/) or [uv](https://github.com/astral-sh/uv) installation.

**Important**. Ensure you're running Gemini CLI from within the 📁 `simple-travel-agent/` folder. Also the IDE should show you this as root name. This ensures Gemini CLI picks up the right configuration. You can always add external folders via `/dir add /your/other/folder`, but 📁 `simple-travel-agent/` provides the **best** initial location.

## Step 1: Basic Agent

Let's start by creating a basic agent that can have a conversation.

Edit the file called `mysolution/__init__.py` by adding the following content:

```python
from .agent import root_agent
```

As simple as that! This allows ADK to know where your code is: in `agent.py`.

Edit the file called `mysolution/agent.py` by adding the following content:

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="travel_basic",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant." +
    "You can help with general travel advice based on your knowledge.",
)
```

<img src="yellow_robot_step1_cli.nb.png" width="40%" align="right">

### Testing the agent

This is true for all the steps. ADK allows you to test your agent in two ways: CLI and Web.

- **CLI** is best for quick and automated tests
- **Web** is the best to visually see what's happening, use microphone (!), and troubleshooting.

**Tip**: for the purpose of this exercise, for everything except unit testing, use the Web. It's really amazing!

A good prompt which properly tests steps 1-2-3-4 can be this (smart "litmus prompt"):

> Hi, I'd like to book a hotel in Paris for tomorrow evening alone, one night, in Paris city center.
> Ideally close to Gare de Lyon. Budget: below 200eur per night.
>
> 1. Tell me which YYYYMMDD and Day of the Week is tomorrow.
> 2. Tell me which hotel do you see for tomorrow (at least 3). I want to see: > price, address, some rating (in form of XX/YY, eg "4.7/5" - from Google Hotels, Booking or Airbnb), # reviews. Give me them in TABULAR format. Ideally, hotel name should be linked to some sort of URL of the hotel (do no bother adding a URL column). Ensure the link is legit (it works and page points to info about the hotel!)

<!-- additional content you might want to add

> 3. Give me a recommendation: what would you choose and why.
> Non negotiable: full apartment, private bathroom, no ground floor in a big city.

-->

This is a smart prompt as it tests time and hotels and will fail differently in steps 1,2,3 and should fully succeed only in step 4. You can of course use any prompt _you_ want!

Run it from bash (CLI):

```bash
# 1. If ADK was installed:
adk run mysolution/
# ... but if you get: -bash: adk: command not found"
# 2. Call ADK cli script through UV to avoid python install nightmares.
uv run adk run mysolution/
```

Try using it the "litmus prompt" above.

It will likely **fail** to know specific dates. We need to teach it to know the date!

<img src="adk_web_select_folder.png" width="30%" align="right">

For web, you can do this:

1. `uv run  adk web .` : This runs all agents under this folder. You want to point it to "mysolution/" subfolder
2. choose `mysolution/` on top right (_See image beside_)
3. Ask your question in text or via microphone something along the lines of the "litmus prompt".

Note you need to call `adk web` from the upper folder, respect to the CLI version.

[Here's](yellow_robot_step1_web.png) a possible solution, with a date semi-hallucination. Note 3 of the 5 booking links are working! Not bad.

## Step 2: Add the `now()` tool

The agent doesn't know what "today" is. Let's give it a tool.

<img src="yellow_robot_step2.nb.png" width="40%" align="right">

Add this function to `agent.py` just before the `root_agent` definition:

```python
from datetime import datetime

def now() -> dict:
    """Returns the current date and time."""
    my_datetime = ... # Ask Gemini CLI to help you!
    return {
        "status": "success",
        "current_time": my_datetime
    }
```

Update the agent definition to include the tool:

```python
    travel_agent = LlmAgent(
        name="..",
        model="..",
        instruction="..",
        tools=[now] # <== This is the only line you want to add.

    )
```

Run it again and ask the same question. It should now know the date (good), and be vague about hotels (bad)!

You can also test it with something like this:

```bash
# LEt's pretend we're in Milan. This should call the tool and respond correctly (possibly with some TZ math issues)
echo "What time is it in Milan?" | uv run adk run mysolution/
```

## Step 3: Let's switch gears: `google_search`

<img src="yellow_robot_step3.nb.png" width="40%" align="right">

Now that we know how to create a custom tool, let's explore how to use one of the powerful built-in tools provided by ADK: `google_search`. This allows our agent to access real-time information from the web.

**Note**: 🚨 `gemini-2.5-flash` cannot natively mix Google Search with custom tools (see [Issue #969](https://github.com/google/adk-python/issues/969) ), so we will **replace** `now()` with `google_search` for simplicity. More details: [docs/ISSUES.md](./docs/ISSUES.md).

Your task is to modify the agent from Step 2. Instead of using the `now` tool, you will import and use the `google_search` tool from the ADK library.

```python
# Full Code: `steps/step03_search/agent.py`
# Remember to REMOVE the now() tool here. See above why.
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="travel_agent",
    model="gemini-2.5-flash",
    tools=[google_search],
    instruction="""You are a travel agent.
Your job is to help the user plan a trip.
You have access to a search engine.
If you don't know the answer, you can use the search engine.
When you are done, reply with "DONE".""",
)
```

### How to Run

Same as per step 1.

**Experts only**. For a more advanced integration (using `google_search` and `now` together), check the code in `steps/step03b_search_and_tool/agent.py` and run it with `just run-step3b`. This is totally optional.

## Step 4: A more sophisticated Tool: MCP

<img src="yellow_robot_step4.nb.png" width="40%" align="right">

Now that we've seen both custom and built-in tools, let's graduate to something more powerful: the **Model-as-a-Tool** pattern using the **Model Context Protocol (MCP)**.

To keep this step focused on the powerful capabilities of MCP, we will once again **replace** our previous tool (`google_search`). We will reintroduce our simple `now` tool to run alongside the `airbnb_mcp` tool. This demonstrates how an agent can use multiple, compatible tools (in this case, a `FunctionTool` and an `MCPToolset`) to perform complex tasks.

```python
# Full Code: steps/step04_mcp/agent.py
# ... Imports as before
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

def now() -> dict:
    # ... as before

# Configure the Airbnb MCP Toolset
airbnb_mcp = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='npx',
            args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"],
        ),
    )
)

root_agent = Agent(
    name="travel_mcp",
    model="gemini-2.5-flash",
    instruction="You are a helpful travel assistant. You can find accommodation using Airbnb, and have access to the current time.",
    tools=[now, airbnb_mcp],
)
```

### How to Run

This step requires `npx` to be installed on your system.
For the rest, this is the same as above.

### Caveats/ Errors

1. If you get a `robots.txt` restriction error, you cn patch the MCP with an ignore robots directive. 
Read the docs for more details: https://github.com/openbnb-org/mcp-server-airbnb

2. If you get a `timeout` error (5 seconds being too low for Airbnb to get responses), look at ADK documentation on how to increase the timeout to, say, 30 seconds. Or.. use Gemini CLI to do it! Note that on 3dec25m Cloud Shell gave me a timoeut error, I fixed the timeout error, and still got errors, until I forced it to the previous versin: `args=["-y", "@openbnb/mcp-server-airbnb@0.1.2", "--ignore-robots-txt"]`. 

## 🏅 Milestone 1 Complete!

🏅 Congratulations! 🏅 **You are now an ADK expert!** You've completed the workshop and have successfully built and tested AI agents with custom tools, built-in tools, and advanced MCP tools. You are now ready to build your own amazing agents with the Google Agent Development Kit!

You now have a functional travel agent that knows the time and can search the web. The sky is now the limit!

Please take a moment to vibecode an additional functionality with "Gemini CLI".

## 🏅 Milestone 2: vibe coding your way through ADK via Gemini CLI

Now we enter the interesting part of the workshop.

1. ensure you have `git commit`ted the code somewhere safe. You can fork the original code, or create a branch: dont worry, Gemini CLI is great at helping you here!
2. Find an 💡 **idea** to implement. You can check the ideas below, find one yourself, or ask Gemini to look at documentation in rag/ and propose a few smart ideas.
3. Follow the **prerequisites** to ensure Gemini _can read_ ADK docs, and then you're good to go!

### 💡 Ideas

Here's a menu with some Ideas of different complexity.

1.  🟢 [easy] Not a python developer? You prefer `go` or `java`? Refactoring the existing code is very simple! Just make sure to download the proper ADK and ask Gemini CLI to do the translation!
1.  🟢 [easy] Add emojis or specify some output format you like (eg, a table with hotel emoji, followed by price, followed by 1-5 star emojis based with 🌕🌕🌕🌗🌑 to do halves too!).
1.  🟢 [easy] Change the prompt to teach it things you're specifically looking for or against (pet-friendly, no ground floor, silent, close to public transport, ..) and test it. Maybe add a personal rating like "a YOUR_NAME-rating from 1-10" based on the above, and sort by that rating.
1.  🟢 [easy] Any Operator in the room? Deploy to [Cloud Run](https://cloud.google.com/run)! Or to [Vertex AI Agent Engine](https://google.github.io/adk-docs/deploy/agent-engine/)! Did you know you can integrate this agent and call it directly from the new **[Gemini Enterprise](https://cloud.google.com/gemini-enterprise)**?
1.  🟢 [easy] Integrate `adk run`` with 🍌 [NanoBanana MCP](https://github.com/ConechoAI/Nano-Banana-MCP). Requires a [Gemini API Key](https://aistudio.google.com/api-keys). Here you'll be able to create images but not visualize them. See below for a harder variant.
1.  🟡 [medium] Create a subagent who does the `HotelSearch` and create a `BudgetAgent` or a `LocationAgent` which can double down and iterate over hotels respecting your location needs, eg "not more than X km from LOCATION". If the API doesn't allow this, it might be some back and forth helped by GoogleSearch. Note: Gemini cLI can help you.
1.  🟡 [medium] Implement a `AirbnbReviewAgent` which goes into the reviews and summarize positives and negatives in a few color-coded bullets, for 1 or N hotels reslting from a search. You already have 2 ingredients (GoogleSearch and MCP Airbnb), then you need to connect this to the main Agent and maybe invent some sort of protocol for them to communicate.
1. 🟡 [medium] Integrate with [A2A](https://github.com/a2aproject/A2A). Make it an A2A agent! Again, ask Gemini CLI for help!
1.  🔴 [complex] You can integrate with Flights or other MCP functionality to create a multi-faceted multi functional travel agent.
1.  🔴 [complex] Integrate ADK web with 🍌 [NanoBanana MCP](https://github.com/ConechoAI/Nano-Banana-MCP). This is harder than the one above, and you can find some tips in https://github.com/palladius/ai-friendly-agents/issues/11 . This took the author 3 hours of back and forth with Gemini CLI, Gemini3 and both of us reading docs/code from `rag/`!

![Adding Geneva image as part of ADK WEB](geneva-in-adk-web.png)

Looking for further inspiration?

1. Check in Maurizio's [great ADK tutorial](https://mauripsale.github.io/doc-adk-training/) for some ideas.
2. Ask Gemini CLI to find ideas by looking at documentation under `rag/`: a possible prompt might be: `Is there a feature in here which seems very succulent to you? Give me 3 proposals and let's implement together the one I choose`.

## Prerequisites for ADK "RAG"

To vibe code a functionality, we recommend that you download the whole ADK [python ADK](https://github.com/google/adk-python) (note: this can be adapted very easily to your favorite language, like [Java](https://github.com/google/adk-java) or [Go](https://github.com/google/adk-go)!)

Code is under `./rag` and can be downloaded with `./download-adk.sh`.

Because the `rag` folder is listed in your `.gitignore` file make sure your `.gemini/settings.json` contains the following:

```json
{
  "context": {
    "includeDirectories": ["rag"]
  }
}
```

**Why?** We want Gemini to be able to read those files, while they're safely git-ignored. Technically you could also unhide all .gitignore files by setting `context.fileFiltering.respectGitIgnore` to `false` but this opens a lot of `node_modules/` and `__pycache__/` garbage - so the explicit folder inclusion is the preferred option.

