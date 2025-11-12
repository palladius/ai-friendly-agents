# Simple Travel Agent

This is a simplified version of the travel agent designed for a step-by-step workshop. It demonstrates the core concepts of the Agent Development Kit (ADK).

## Workshop Goals

By following the [`WORKSHOP.md`](WORKSHOP.md) guide, you will learn the fundamentals of the Google Agent Development Kit (ADK) through a clear, progressive path:

1.  **Step 1: Create a Basic Agent:** Build your very first, simple ADK agent.
2.  **Step 2: Add a Custom Tool:** Enhance your agent by **adding** a custom Python date function (`now()`) as a tool.
3.  **Step 3: Use a Built-in Tool:** Learn how to use powerful, pre-built tools by **replacing** your custom tool with `google_search`.
4.  **Step 4: Integrate with MCP:** **Replace** the search tool with an MCP (Model Context Protocol) tool, showing how to connect to external services and use multiple compatible tools together.

This "add -> replace -> replace" approach is designed to isolate and teach each core concept effectively. For advanced users, the workshop also includes an optional step (`step03b`) that demonstrates how to make `google_search` and custom tools work together (see [issue 969](https://github.com/google/adk-python/issues/969) for the limitation).

## Getting Started

Make sure you have `uv` installed for dependency management.

```bash
# Install dependencies
uv sync
```

Start the workshop by following the instructions in [`WORKSHOP.md`](WORKSHOP.md).
