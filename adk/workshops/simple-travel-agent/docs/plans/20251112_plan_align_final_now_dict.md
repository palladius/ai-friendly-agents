[GitHub Issue #9](https://github.com/palladius/ai-friendly-agents/issues/9)

# 🇫🇷 Align Workshop Docs and Code (Final: `now()` returning `dict`)

We are aligning everything to use `now()` (matching images) and returning a `dict` (best practice/user requirement).

- [ ] **Update `WORKSHOP.md`**
    - [ ] Step 2: Change function name to `now`.
    - [ ] Step 2: Change return type hint to `-> dict`.
    - [ ] Step 2: Change implementation to return `{"current_time": ...}`.
    - [ ] Step 2: Register `tools=[now]`.
    - [ ] Step 4: Update `get_now` to `now` and ensure it returns `dict`.

- [ ] **Update Code in `steps/`**
    - [ ] `steps/step02_tool/agent.py`: Rename `get_now` -> `now`, type hint `-> dict`, ensure returns dict.
    - [ ] `steps/step03_search/agent.py`: Rename `get_now` -> `now`, type hint `-> dict`, ensure returns dict.
    - [ ] `steps/step03b_search_and_tool/agent.py`: Rename `get_now` -> `now`, type hint `-> dict`, ensure returns dict.
    - [ ] `steps/step04_mcp/agent.py`: Rename `get_now` -> `now`, type hint `-> dict`, ensure returns dict.

- [ ] **Verify**
    - [ ] Run `just test-whole-workshop`.
