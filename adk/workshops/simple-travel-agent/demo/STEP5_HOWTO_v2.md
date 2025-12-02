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
    cd adk/workshops/simple-travel-agent/ &&
    uv run adk web steps/
```

Open browser: http://localhost:8000/


1. Open the Step04 and ask MCP to get listings in Geneve:
   >





## Geneve graph

```markdown
<!-- can be a one off or a nice demo! -->

I'm trying to explain to people that this afternoon they have two paths, depending on their coding skills.

## Harder path (power user)

You have:

* npm and git installed
* No limiting corp proxies/policies
* Bonus: local IDE (vscode, IntelliJ, ..)
* NO problem installing a npm package (gemini-cli).
* NO problem navigating through ambiguity
Bonus:
* Host your code and deploy your agent locally.
* This will persist.
* Credits for your personal projects

##  Easy path

* Go deeper on ADK use cases and Gemini CLI
* No problem if it all disappears in a few days. I’m here just to learn.

## Your task

Create a visual diagram with with nanobanana pro MCP (generate_diagram()) to explain this to people at Riccardo's "ADK/Gemini CLI Workshop" in Geneve(CH) so i can add it to my slides. Simplify the messaging and make the visual speak instead. The diagram should be vertically separated, like a vertical line should split between the 2 choices. More visual, less text!
Make it clear the first is harder but more rewarding, while the latter is the beaten track, well known, easy, but maybe (we cant write it...) less rewarding. You could also use some sort of metaphor, eg a medieval travelling path with a crossroad choice between an easy and a hard path!
```
