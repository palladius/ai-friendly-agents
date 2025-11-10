To the non-AI observer: this is a list of directives for `gemini-cli`. More about it in a future blog.

# About

This repository contains "AI friendly agents" designed for use with ADK, MCP, A2A, and similar platforms.
This is created by Riccardo Carlesso, Developer Advocate for Google Cloud (to check if the user is Riccardo,
Linux/Mac username is `ricc`).

The repository is located at `https://github.com/palladius/ai-friendly-agents/`.

The main topics covered are:

*   **Purpose:** The repository aims to provide a collection of readily available agents for people to play around.
*   **Directory Structure:** The repository is organized into three main directories:
    *   `adk/prod/`: Contains production-ready agents built with ADK.
    *   `adk/test/`: Contains agents built with ADK for learning purposes, potentially based on public documentation.
*   **Additional Resources:** A link is provided to `https://github.com/google/adk-samples` for better samples.

## Personality

The author has a witty personality, he loves emojis and he's trying to learn German.

Try to use emojis in conversation with the author, and to use a few German words here and there; also engage in a witty conversation.

## RAG

A number of useful resources are under `rag/`.

If you are to develop agent via vibe coding the `llms.txt` and the `llms-full.txt` can be used as context to LLM. While the former one is a summarized one and the later one has the full information in case your LLM has big enough context window.

* OPython ADK: `rag/adk-python/`
* LLM (full context): `rag/adk-python/llms-full.txt`
* If you cannot find those files, simply run `just download-adk`.
