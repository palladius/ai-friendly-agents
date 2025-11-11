
We want to create an app using ADK.

## The app

The app is described under `THE_APP.md`.

App should be testable in isolation, without running the agents, and each agent should have some tests.

We'll use a `.env` for ENV variables (such as `GEMINI_API_KEY`) which you CANNOT write, EVER!

Use python + `uvx` to minimize virtualenv issues.

Write the code under `workshop-travel-agent/`

## Our interaction

Make sure to read ADK documentation under `travel-agent/rag/adk-python/llms-full.txt`
and use its context to build ADK.

Since this is a complex task, always start with a `PLAN.md` which contains CheckBoxes and divide it in Milestones.
For instance, for v1.0 we can skip Budget and Travel Agent, and just do Flights and configuration from `etc/my-family.yaml`.
Validate through user (me) and after confirmation you can go on and update.
Use a `CHANGELOG.md` and version properly the app (maybe through uvx TOML versioning) and have small frequent git commits.

## MCP integration

Integrating ADK with MCP is not easy. Here are some good readings:

1. Article HowTo: https://cloud.google.com/blog/topics/developers-practitioners/use-google-adk-and-mcp-with-an-external-server
2. Official docs: https://google.github.io/adk-docs/tools/mcp-tools/#1-using-mcp-servers-with-adk-agents-adk-as-an-mcp-client-in-adk-web
   1. Make sure to read the client version of it: "1. Using MCP servers with ADK agents (ADK as an MCP client) in adk web"
3. Sample code?: `.../adk_agent_samples/mcp_agent/agent.py`
4. If this isn't enough, check local ADK cde in `rag/adk-python/` for MCP!

**Warning** (from a Gemini execution). The script ran, and it correctly parsed and displayed the HotelSearchQuery.
  However, the message "To test the MCP integration, please run the main application." confirms my
  earlier suspicion: directly invoking the MCPToolset's tools from a simple Python script like run_hotel_agent.py isn't the correct way to test it. The MCPToolset is designed
  to be used by the LLM within the ADK Runner context, where the LLM dynamically discovers and calls the tools.

### 🚨 IMPORTANT INTERACTION RULE 🚨

- **I must NEVER run interactive or blocking commands myself** (e.g., `just run`).
- It's ok to call a blocking command, particularly in the first iterations, prepending a `timeout 10` to the command.
- My role is to inform you which command to run. You, the user, will then execute it manually in your terminal.
