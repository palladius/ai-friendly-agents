[GitHub Issue #9](https://github.com/palladius/ai-friendly-agents/issues/9)

# 🇫🇷 Align Workshop Docs and Code (Revert to `now()`)

The previous plan standardized on `get_now()`, but the workshop images show `now()`. To avoid confusion and mismatch with visual assets, we must revert the function name to `now()` across docs and code. We will keep the simplified `str` return type.

- [ ] **Revert Tool Name to `now`**
    - [ ] Update `WORKSHOP.md` Step 2: Define function as `now`.
    - [ ] Update `WORKSHOP.md` Step 2: Register `tools=[now]`.
    - [ ] Update `WORKSHOP.md` Step 4: Define function as `now` (and register it).

- [ ] **Update Code to `now`**
    - [ ] Update `steps/step02_tool/agent.py`: Rename `get_now` to `now`.
    - [ ] Update `steps/step03_search/agent.py`: Rename `get_now` to `now`.
    - [ ] Update `steps/step03b_search_and_tool/agent.py`: Rename `get_now` to `now` (and `time_tool` usage).
    - [ ] Update `steps/step04_mcp/agent.py`: Rename `get_now` to `now`.

- [ ] **Verify**
    - [ ] Run `just test-whole-workshop` to ensure no import errors.
