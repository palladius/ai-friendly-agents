**Note**: Once the workshop is done, we need to re-write this GEMINI.md!!!

## Workshop creation

* Whenever possible, inherit or learn from the more-complex, mostly-working code in `../complex-travel-agent/`.
* For ease of TESTING, let's ensure we have code in python which we can then test manually.
* Let's ensure we have a folder "sample_code/" with sample code:
  * python code for the agent
  * a library subfolder for tools and "less visible code"
  * a test folder to test python. Tests should return fast, lets concentrate on Unit tests for now.
  * a `Justfile` with some sample invocations: `just test`, `just list`, ..
  * Some commented code for the next step. Example: a perfectly defined Tool function,
    commented out,
  * A `pyproject.toml` for `uv`. We use `uv` and `uvx` to execute python with automatic library installation which doesn't depend on sourcing `.env`. This is because
* To ensure ease between student code and solution, we probably need to mirror the code into a `.solutions/` secret folder with FULLY working code. This way we can easily go back and forth between the REAL solution and the half-baked solution we give to students.

## Code creation

Let's ensure Gemini CLI is able to read ADK code

* Download Google ADK locally. To do this, execute `./download-adk.sh`.
* Read Google ADK python library under `./rag/adk-python/`.
* Before writing code for ADK, make sure you at least read docs in `rag/adk-python/llms-full.txt` but be prepared to fully leverage the codebase for complex tasks like adding MCP client or tooling or deploying to Cloud Run / Vertex AI.
* If you can't read the folder, work with user to add this config to `.gemini/config.json`:

```json
{ "fileFiltering": {
    "respectGitIgnore": false
  }
}
```
* Consider using `git grep` for git checked-in code, such as simple and complex travel agent (Note: this won't work for adk-google, since that is git-ignored).
* If user pings you a public doc (eg 'Use Built-in tools with other tools'), try to execute this command, and it will likely work! `grep 'Use Built-in tools with other tools' rag/`.

## testing

Ensure all versions of the workshop are tested.
For instance:

```bash
# This works
echo "I'd like to book a hotel in milan for next Tuesday, Im alone and have no budget preference." | uv run adk run steps/step01_basic/

# This is broken
echo "Same test as above" | uv run adk run steps/step02_tool/
[...]
ImportError: Fail to load 'step02_tool' module. cannot import name 'tool' from 'google.adk.tools' (/usr/local/google/home/ricc/git/ai-friendly-agents/adk/workshops/simple-travel-agent/.venv/lib/python3.13/site-packages/google/adk/tools/__init__.py)
[..]
```

## ADK Web

ADK web is great for user troubleshooting.
However, it has a weird folder caveat.

Note that `adk web` needs a super-folder for agents to be tested, so we can test all steps this way:

```
# Run Step 1/2/3/4 in Web UI
web-4steps:
    uv run adk web steps/
```

Note: `adk web steps/step1/` WILL NOT WORK. (I know!)

## WORKSHOP.md (the readme)

The workshop README (WORKSHOP.md) should do a few things:

1. Ensure the code in steps/.. is in sync with steps 1,2,3,4 f the workshop! this is VERY important.
2. User is supposed to build their solutions under `mysolution/`.
