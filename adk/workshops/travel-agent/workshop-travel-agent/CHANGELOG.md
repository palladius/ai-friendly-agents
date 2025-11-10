# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2025-11-10
### Changed
- Prioritized `HotelAgent` MCP integration.
- Re-created `etc/sample-hotel-query.yaml` and `src/run_hotel_agent.py` for isolated testing.
- Re-added `run-hotel-agent` recipe to `justfile`.
- Refactored `HotelAgent` to use `MCPToolset` with `StdioConnectionParams` for Airbnb MCP.

## [0.6.0] - 2025-11-10
### Changed
- Refactored logging to be agent-specific. Each agent now creates its own log file in the `log/` directory.

## [0.5.0] - 2025-11-10
### Added
- Implemented the `HotelAgent` with mock data.
- Integrated the `HotelAgent` as a sub-agent of the `ConciergeAgent`.
- Added tests for the `HotelAgent`.

## [0.4.0] - 2025-11-10
### Added
- The `Concierge` agent now greets the first person in the family list by name.
- Added a test to verify the personalized greeting.

## [0.3.0] - 2025-11-10
### Added
- The `Concierge` agent now proposes a default travel plan.
- Added a `get_default_travel_dates()` tool to calculate the next two Saturdays.
- Added a test to verify the default travel plan proposal.

## [0.2.0] - 2025-11-10
### Added
- The `Concierge` agent can now use the `now()` tool to get the current date and time.
- The agent can read a family configuration file to personalize its interaction.
- The application accepts a `-f`/`--file` command-line argument to specify the configuration file.
- Added tests for the new functionality.

## [0.1.0] - 2025-11-10
### Added
- Initial project setup with `uv`.
- Created `src` and `tests` directories.
- Added `.gitignore` and `CHANGELOG.md`.
- Implemented configuration loading from `etc/sample-family.yaml`.
- Defined data classes for configuration (`Family`, `Person`, `Address`, `TravelProps`, `Budget`).
- Added unit test for configuration loading.
- Created basic `Concierge` agent structure using `LlmAgent`.
- Added `google-adk` dependency.

## [Unreleased]
