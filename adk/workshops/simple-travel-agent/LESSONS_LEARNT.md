# Lessons Learnt (NanoBanana MCP Integration)

## 1. `MCPToolset` Iteration / Tool Access
- **Mistake:** Attempted to iterate directly on an `MCPToolset` object or call a non-existent `get_tool()` method (e.g., `nanobanana_mcp.get_tool()`).
- **Correction:** The correct way to access individual tools within an `MCPToolset` is via its `tools` property (e.g., `next((t for t in nanobanana_mcp.tools if t.name == 'tool_name'), None)`).

## 2. `StdioServerParameters` Environment Variable Naming
- **Mistake:** Used `environment={...}` instead of `env={...}` when passing environment variables to `StdioServerParameters`.
- **Correction:** The correct parameter name is `env`.

## 3. `StdioConnectionParams` Timeout Parameter Naming
- **Mistake:** Used `timeout=` instead of `timeout_in_seconds=` for setting the client connection timeout in `StdioConnectionParams`.
- **Correction:** The correct parameter name is `timeout_in_seconds`.

## 4. `uv run` and Environment Variable Loading in Justfile
- **Mistake:** Incorrectly assumed a `--with-dotenv` flag for `uv run` (which does not exist) or used `.` sourcing in Justfile without properly escaping the command for `uv run` to inherit environment variables when `adk web` is run in a subprocess.
- **Correction:** The `.` (source) command in `bash` is needed to correctly export environment variables before `uv run`. `just` executes each command in its own shell, so it requires explicit sourcing. (Further investigation needed to confirm if `uv run`'s subprocess environment for the MCP server is inheriting correctly even with correct sourcing).

## 5. Trusting My Own Cache/Memory (Critical!)
- **Mistake:** Repeatedly made similar errors or attempted to fix issues that were already resolved in the code, indicating a severe disconnect between my internal state/memory and the actual file content. This led to wasted time and increased user frustration.
- **Correction:** ALWAYS use `read_file` or `search_file_content` to *verify* current file content before attempting any modification, especially when previous attempts have failed or when the user indicates an existing state. Do not rely on cached information or assumptions.

## 6. Understanding ADK's MCP Connection Paradigm
- **Mistake:** Attempted to manually manage MCP server processes and environment variables within the agent's code (`StdioConnectionParams`) when the `gemini-cli` already has a robust, pre-configured connection (`McpCliConnectionParams`) for common MCP servers like NanoBanana.
- **Correction:** When a `gemini-cli`-managed MCP server is available and working (e.g., `nanobanana-cinese`), leverage `McpCliConnectionParams(server_name="<server_name>")` directly in the agent's `MCPToolset` configuration. This delegates server lifecycle and environment management to `gemini-cli`, simplifying the agent's code and improving reliability.

## 7. The Timeout Mystery
- **Current Unresolved Issue:** Despite `timeout_in_seconds=60` being set in `StdioConnectionParams` in `agent.py`, the client still reports `Waited 5.0 seconds.` This indicates a deeper problem with how the timeout is applied or inherited by the MCP client when the server is launched via `uvx` within `adk web`. This is currently beyond my ability to diagnose.
- **Next Steps (Human Intervention):** This specific issue requires human expertise to debug the interaction between ADK, uvx, and the MCP client/server timeout mechanisms, potentially at a lower level than I can access.
