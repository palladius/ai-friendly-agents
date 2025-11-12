[GitHub Issue #9](https://github.com/palladius/ai-friendly-agents/issues/9)

# 🇫🇷 Align Workshop Docs and Code

The goal is to ensure `WORKSHOP.md` and the solution code in `steps/` are consistent, specifically regarding the `get_now` tool. We will favor the simpler implementation (returning a string) described in the docs, and update the code to match it, while fixing naming inconsistencies.

- [ ] **Standardize Tool Name to `get_now`**
    - [ ] Update `WORKSHOP.md` Step 2 to define the function as `get_now` (currently `now`).
    - [ ] Update `WORKSHOP.md` Step 2 to register `tools=[get_now]`.

- [ ] **Align Code Implementation (Simpler is Better)**
    - [ ] Update `steps/step02_tool/agent.py`: Change `get_now` to return `str` (just the date string), matching the doc's simple logic. Fix type hint.
    - [ ] Update `steps/step03_search/agent.py`: Sync `get_now` implementation (even if unused/replaced, it's good practice).
    - [ ] Update `steps/step04_mcp/agent.py`: Sync `get_now` implementation.

- [ ] **Verify Documentation Flow**
    - [ ] Ensure `WORKSHOP.md` Step 3 text correctly refers to `get_now` when discussing replacement.
