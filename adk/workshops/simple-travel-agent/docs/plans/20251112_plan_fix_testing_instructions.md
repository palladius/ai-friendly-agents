[GitHub Issue #9](https://github.com/palladius/ai-friendly-agents/issues/9)

# 🇫🇷 Fix Testing Instructions in Workshop

The user pointed out that the "How to Run" instructions in Step 3 and Step 4 incorrectly point to the *solution* code (`just run-step3`) instead of the user's work in `mysolution/`.

We need to update these sections to emphasize the iterative development loop:
1.  Modify code in `mysolution/`.
2.  Restart the agent/web UI.
3.  Test against `mysolution/`.

- [ ] **Update Step 3 "How to Run"**
    - [ ] Remove `just run-step3`.
    - [ ] Instruct user to restart `adk web` (CTRL-C + `uv run adk web .`) and select `mysolution`.
    - [ ] Keep the "Experts only" note about `step03b` but make sure it's clear it's a separate thing.

- [ ] **Update Step 4 "How to Run"**
    - [ ] Remove `just run-step4`.
    - [ ] Instruct user to restart `adk web` and select `mysolution`.
    - [ ] Mention `npx` requirement is for the *agent* execution.

- [ ] **Verify**
    - [ ] Read the file to ensure flow makes sense.
