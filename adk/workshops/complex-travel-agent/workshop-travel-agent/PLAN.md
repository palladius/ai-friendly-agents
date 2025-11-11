# Travel Agent Workshop Plan

This plan outlines the steps to add file I/O capabilities to the Concierge agent and improve the application's observability.

## Milestone 1: Refactor File Tools and Stabilize Tests

- [x] **Refactor File I/O Tools into a Shared Library**
  - [x] Create `src/lib/` directory.
  - [x] Create `src/lib/file_tools.py`.
  - [x] Move `write_plan`, `list_plans`, and `read_plan` from `src/tools.py` to `src/lib/file_tools.py`.
  - [x] Update `src/concierge_agent.py` to import file tools from the new library.
  - [x] Update `tests/test_plan_tools.py` to import from the new library.

- [ ] **Fix Agent Tests**
  - [ ] Refactor `tests/test_flight_agent.py` to mock the `MCPToolset` directly and fix assertions.
  - [ ] Refactor `tests/test_hotel_agent.py` to mock the `MCPToolset` directly and fix assertions.
  - [ ] Refactor `tests/test_concierge_agent.py` to use more flexible assertions for the agent's greeting.

- [ ] **Verify Changes**
  - [ ] Run `just test` and ensure all tests pass with a timeout.

## Milestone 2: Implement Enhanced Observability

- [ ] **Capture and Display Thought Signatures**
  - [ ] Modify the main application loop to access the full `candidates.content.parts`.
  - [ ] Extract the `thought_signature` when present.
  - [ ] Implement a function to print the thought signature in dark gray with a 🧠 emoji.

- [ ] **Implement Colored Logging**
  - [ ] Create a custom logging formatter or utility for colored output.
  - [ ] Color the main `ConciergeAgent` output WHITE.
  - [ ] Color ADK WARNINGS in ORANGE.

- [ ] **Final Verification**
  - [ ] Run the application (`just run-concierge-testing-hotel-agent`) to visually confirm all new formatting and logging works as expected.
  - [ ] Update `CHANGELOG.md` with all the new features.
