
We want to create a complex Travel agent. You can add this to the `GEMINI.md` and start asking question and guide code development.

git clone https://github.com/palladius/ai-friendly-agents/ then cd  to `adk/workshops/travel-agent`.

1. Enter the folder.
1. Execute `./download-adk.sh` to download ADK code, this will be useful.
1. Ensure you configure the `.gemini/settings.json` to NOT follow .gitignore.

## Note to self

Riccardo, this workshop tries to build a COMPLEX (maybe TOO complex!) ADK agent.

1. Concierge - talks to you and delegates to others.
2. Hotel Agent. Can simply talk to AirBNB via StDIO MCP (*Easy*)
3. Flight Agent. Can talk to Google flights via MCP - buit no code written simply yet (not a simple `npx -y code` yet -> *harder*).

So probably you should be the Hotel agent first.

## First prompt

Moved to `GEMINI.md`


## Let's add some Feature  / tests

### [FR+Test] concierge salutation

**What is this?** This adds a nice touch to the day-0 experience to user, and adds a good test. Note that the LLM is going to likely greet "Riccardo"
so we can test deterministically for the word "Riccardo" in it. Strings are easier to test than dates, within an LLM context.

We can ask the Concierge agent to be programmed to always greet the first person specified in the YAML `Family:` array.


### [FR] Logging

```markdown
<!-- This provides logging to our app: set it up earlier than later! -->
Now we need to Log all the agent does.
Each Agent should have a `-l/--log` LOGFILE, and default to "log/agent_name.log" (with `mkdir` of log if needed,
or just `git add log/.keep` to keep it easy).
```

### [FR] MCP AirBnb (Easy)

```markdown
<!-- TODO ricc:
 -->
Let's now start to create the SIMPLE MCP Client: the hotel agent. This can use this MCP natively:
* Docs: https://github.com/openbnb-org/mcp-server-airbnb
* Command: `npx -y @openbnb/mcp-server-airbnb`
* HowTo: https://cloud.google.com/blog/topics/developers-practitioners/use-google-adk-and-mcp-with-an-external-server
* HowTo: https://google.github.io/adk-docs/tools/mcp-tools/#1-using-mcp-servers-with-adk-agents-adk-as-an-mcp-client-in-adk-web
I want to be able to test this in isolation, so something like a `etc/sample-hotel.yaml` in input.
You should use something like `pydantic` to set a "rigid" and testable input for this.
Check parameters described in https://github.com/openbnb-org/mcp-server-airbnb and make sure to implement the simplest
of them (location, checkin, checkout, adults, children, infants, maxPrice should be enough to get started).
```

### [FR] Add Saving trip info to disk

This is something that Gemini cLI can do natively, for ADK we need to do it manually.

```markdown
We want now for the Concierge agent to be able to WRITE to disk.
We need to have two tools where we can dump a sample

## `write_plan(plan_name: str, date: date, content: str, plan_id: int=1 )`
* output dir: `out/travel_plans/`.
* Creates a folder:  `out/travel_plans/202511_RomanticWeekendInMilan/`. Using YYYYMM of the
* creates a `PLAN_1.md` (we might have multiple plans and refine them over time).
* Have some prompt to instruct Gemini model to write PLAN in a certain way:
    * Multiple choices should be in tabular mode
    * Always start with a synoptic
    * Links are cheap! Let's link all we have
    * Less is more: better a linked title than both the title and a self-linked link, which occupies much more space!

## `list_plans()`
* Allow to explore existing plans

## `read_plans(src: "path/to/file_xx.md")`
* reads file and provides to user. This can be a good way to continue/refine an old plan.

```

### [FR] MCP Implementation (hard)

```markdown
<!-- This creates the first complex interaction of the day: we want agent to do sth complicated, and to have a predictable structure in input.
     And we're simply vibecoding it! Let's ensure a PLAN is written.
 -->
Now I want the flight to use the MCP! Lets create it, and lets test it in isolation. We need to find a way we can feed a sample flight to it,
like with `--flight/-f etc/sample-flight.yaml` or similar, you can find a way.
Probably we need some `pydantic` or similar to have a strict protocol to interact (2 ADULT/CHILDREN, DATE_START, ECONOMY/BUSINESS, airport_code, ...).
User should be able to specify things in english like "prioritize single track over cost", maybe for a post-API-call review.
Try these MCPs:
- https://mcpmarket.com/server/google-flights
- https://github.com/salamentic/google-flights-mcp
Or build your own using SERP API :)
Use ADK documentation for MCP here: https://google.github.io/adk-docs/tools/mcp-tools/#1-using-mcp-servers-with-adk-agents-adk-as-an-mcp-client-in-adk-web
(the first chapter: "1. Using MCP servers with ADK agents (ADK as an MCP client) in adk web")
```

