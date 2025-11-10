
Self: https://github.com/palladius/ai-friendly-agents/ (public)

# About

This repo provide easy ready-to-use agents which work with the Python ADK library.

More on ADK:

* https://github.com/google/adk-python
* https://google.github.io/adk-docs/

## Breaking changes

Currently some agents are broken. I've added a dangerous change.

However, a stable version is available here: https://github.com/palladius/ai-friendly-agents/tree/v0.9/

# AI friendly agents

A bunch of friendly agents ready to use with ADK, MCP, A2A et al.

Dir structure:

* `adk/prod/`: agents built with ADK. Production ready, ready to use.
* `adk/dev/`: agents built with ADK. More to learn how to do things. Could be cut and paste of public docs.
* `mcp-agents/prod`: agents built with MCP. Production ready, ready to use.
* `mcp-agents/dev`: agents built with MCP. More to learn how to do things.
* `rag/`: samples to instruct AIs with local code.

Better samples can be found here: https://github.com/google/adk-samples

## MCP

To test MCP agents:

* Nice locally running agent: `npx @modelcontextprotocol/inspector`
* Use the `pip install mcp[cli]`. Never tried yet. [Example](https://github.com/ilyazub/serpapi-mcp-server/tree/main).

# Install

First, install `ADK` for python: `pip install google-adk`

```bash
# 1. Clone and adapt env file
git clone https://github.com/palladius/ai-friendly-agents/
cp .env.dist .env
# edit away .env with your info

# 2. Install virtualenvenv
python -m venv .venv
source .venv/bin/activate

# 3.
cd adk/prod/
pip install -r requirements.txt
```

