
We want to create a complex Travel agent. You can add this to the `GEMINI.md` and start asking question and guide code development.

git clone https://github.com/palladius/ai-friendly-agents/ then cd  to `adk/workshops/travel-agent`.

1. Enter the folder.
1. Execute `./download-adk.sh` to download ADK code, this will be useful.
1. Ensure you configure the `.gemini/settings.json` to NOT follow .gitignore.


## First prompt

Moved to `GEMINI.md`


## Let's add some tests

### concierge salutation

**What is this?** This adds a nice touch to the day-0 experience to user, and adds a good test. Note that the LLM is going to likely greet "Riccardo"
so we can test deterministically for the word "Riccardo" in it. Strings are easier to test than dates, within an LLM context.

We can ask the Concierge agent to be programmed to always greet the first person specified in the YAML `Family:` array.


### Logging


Now we need to Log all the agent does.
Each Agent should have a -l/--log LOGFILE, and default to "log/agent_name.log" (with mkdir of log if needed, or just git add a
log/.keep to keep it easy).
