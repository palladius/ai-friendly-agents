# Workshop Travel Agent - Development Plan

This document outlines the development plan for the Workshop Travel Agent.

## Milestone 1: Core Infrastructure (v0.1.0)

- [x] **Project Setup:**
    - [x] Initialize a Python project using `uv`.
    - [x] Create a `pyproject.toml` file with basic project metadata (name, version, description).
    - [x] Create a `src` directory for the application code.
    - [x] Create a `tests` directory for the unit tests.
    - [x] Add a `.gitignore` file.
    - [x] Create a `CHANGELOG.md` file.
- [x] **Configuration:**
    - [x] Create a simple configuration loader to read the `etc/sample-family.yaml` file.
    - [x] Define data classes for the configuration (e.g., `Family`, `TravelProps`, `Budget`).
- [x] **ADK Agent Setup:**
    - [x] Create the basic structure for the `Concierge` agent.
    - [x] Implement a simple "hello world" for the `Concierge` agent to ensure it's working.

## Milestone 2: The Core Engine (v0.2.0)

- [x] **Implement `Concierge` Agent (`Androsthenes`):**
    - [x] Implement the logic for the `Concierge` agent to interact with the user and gather travel details.
    - [x] The `Concierge` agent can now use the `now()` tool to get the current date and time.
    - [x] The agent can read a family configuration file to personalize its interaction.
    - [x] The application accepts a `-f`/`--file` command-line argument to specify the configuration file.
    - [x] The `Concierge` agent should be able to handle default values as described in `THE_APP.md`.
    - [x] The `Concierge` agent now greets the first person in the family list by name.
- [x] **Implement `Flight` Agent (`Fabio Volo`):**
    - [x] Create the `Flight` agent.
    - [x] Implement the logic to search for flights. For now, this can be a mock implementation that returns static data.
- [x] **Implement `Hotel` Agent (`Barabba`):**
    - [x] Create the `Hotel` agent.
    - [x] Implement the logic to search for hotels. For now, this can be a mock implementation that returns static data.
- [x] **Agent Interaction:**
    - [x] The `Concierge` agent should be able to call the `Flight` and `Hotel` agents.
- [x] **Logging:**
    - [x] Implement logging to a file.
    - [x] Add a `-l`/`--log` command-line argument to specify the log file.

## Milestone 3: Integration and Refinement (v0.3.0)

- [ ] **Integrate MCP Servers:**
    - [ ] Integrate the `Flight` agent with the Google Flights MCP server.
    - [ ] Integrate the `Hotel` agent with the AirBNB MCP server.
- [ ] **Testing:**
    - [ ] Write unit tests for the configuration loader.
    - [ ] Write unit tests for the agents (using mocks for external services).
- [ ] **Documentation:**
    - [ ] Update the `README.md` with instructions on how to set up and run the application.

## Future Milestones (v1.0.0 and beyond)

- [ ] **Implement `Budget` Agent (`Scrooge`):**
    - [ ] Create the `Budget` agent.
    - [ ] Implement the logic to calculate the travel budget.
- [ ] **Implement `Travel` Agent (`Antiochus`):**
    - [ ] Create the `Travel` agent.
    - [ ] Implement the logic to provide travel recommendations.
- [ ] **Output:**
    - [ ] Implement HTML/PDF output of the travel plan.
- [ ] **State Management:**
    - [ ] Implement state management to allow for plan amendments.