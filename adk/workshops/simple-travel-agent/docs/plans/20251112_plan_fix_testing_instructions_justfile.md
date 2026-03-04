[GitHub Issue #9](https://github.com/palladius/ai-friendly-agents/issues/9)

# 🇫🇷 Fix Testing Instructions with Justfile Targets

The user wants to simplify testing of their own solution (`mysolution/`) by adding `Justfile` targets.

- [ ] **Update `Justfile`**
    - [ ] Add `run-mysolution`: `uv run adk run mysolution/` (CLI)
    - [ ] Add `web-mysolution`: `uv run adk web .` (Web UI)

- [ ] **Update `WORKSHOP.md` Step 3**
    - [ ] Replace `just run-step3` with instructions to use `just web-mysolution` (preferred) or `just run-mysolution`.
    - [ ] Emphasize the "Edit -> Restart -> Test" loop.

- [ ] **Update `WORKSHOP.md` Step 4**
    - [ ] Replace `just run-step4` with `just web-mysolution`.

- [ ] **Verify**
    - [ ] Check `Justfile` syntax.
