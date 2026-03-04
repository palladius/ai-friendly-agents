# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2025-11-11

### Added
- Created the initial "Simple Travel Agent" ADK workshop with 4 progressive steps.
- Step 1: A basic agent setup.
- Step 2: Introduction of a custom `get_now` function tool.
- Step 3: Integration of the built-in `google_search` tool.
- Step 4: Advanced integration with the Airbnb MCP toolset.
- Added a `Justfile` with convenient commands (`run-stepX`, `web-stepX`, `test-whole-workshop`) to easily run and test each part of the workshop.
- Included `pyproject.toml` for streamlined dependency management with `uv`.
- Added `test_workshop.py` script to verify that all agent steps are importable and syntactically correct.

### Fixed
- Corrected tool implementation to use ADK's automatic function-to-tool wrapping, removing erroneous `@tool` decorator.
- Refactored tool usage in steps 3 and 4 to accommodate `gemini-2.5-flash` model limitations regarding mixing Grounding (`google_search`) with other function-calling tools.
