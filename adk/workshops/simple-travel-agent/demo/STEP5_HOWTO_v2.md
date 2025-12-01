# How to clone and setup the AI Friendly Agents repo (Step 5 Branch)

Here are the commands to clone the repository, ensure all branches are fetched, and check out the specific step 5 branch.

```bash
# 1. Clone the repository into a specific directory
# This clones the default branch (usually main) into the target folder
git clone git@github.com:palladius/ai-friendly-agents.git ~/git/ai-friendly-agents-step5-branch/

# 2. Enter the directory
cd ~/git/ai-friendly-agents-step5-branch/

# 3. Ensure we are tracking ALL remote branches 
# (Useful if the repo was cloned with restrictions or just to be safe)
git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'

# 4. Fetch all latest updates from all branches
git fetch --all

# 5. List all available branches to verify
git branch -a

# 6. Checkout the specific branch for the workshop step 5
git checkout 20251127-step5

## FAQ: Why don't I see all branches locally?

Git fetches all "remote" branches (visible via `git branch -a`), but it doesn't create a "local" copy for every single one automatically.

To create a local copy of another remote branch (e.g., `main`), just check it out:

```bash
git checkout main
```

Git will automatically set it up to track `origin/main`.

## test

```bash
cd ~/git/ai-friendly-agents-step5-branch/
git checkout 20251127-step5
find adk/workshops/simple-travel-agent/ | grep step05 &&
    cd adk/workshops/simple-travel-agent/steps/ &&
    adk web
```
 should have the 5th step: `adk/workshops/simple-travel-agent/steps/step05_mcp2_nanobanana`

> **Note:** If this folder is missing, you are likely still on the `main` branch! Run `git checkout 20251127-step5` to fix it.


## Demo

If this works: 

```bash
cd ~/git/ai-friendly-agents-step5-branch/ &&
    git checkout 20251127-step5 &&
    find adk/workshops/simple-travel-agent/ | grep step05 &&
    cd adk/workshops/simple-travel-agent/steps/ &&
    adk web
```

Open browser: http://localhost:8000/