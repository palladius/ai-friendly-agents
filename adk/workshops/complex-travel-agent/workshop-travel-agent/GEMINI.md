
We want to create an app using ADK.

## The app

The app is described under `THE_APP.md`.

App should be testable in isolation, without running the agents, and each agent should have some tests.

We'll use a `.env` for ENV variables (such as `GEMINI_API_KEY`) which you CANNOT write, EVER!

Use `python` + `uvx` to minimize virtualenv issues.

Write the code under `workshop-travel-agent/`.

## Our interaction

Make sure to read ADK documentation under `travel-agent/rag/adk-python/llms-full.txt`
and use its context to build ADK.

Since this is a complex task, always start with a `PLAN.md` which contains CheckBoxes and divide it in Milestones.
For instance, for v1.0 we can skip Budget and Travel Agent, and just do Flights and configuration from `etc/my-family.yaml`.
Validate through user (me) and after confirmation you can go on and update.
Use a `CHANGELOG.md` and version properly the app (maybe through uvx TOML versioning) and have small frequent git commits.

## Documentation

1. Keep a README.md updated with what has been implemented.
2. Have a minimalistic `justfile` with meaningful commands, such as:
    `just list`: list targets
    `just test`: runs all tests
    `just run`: runs the concierge in interactive mode
    `just run-with-sample-payload`: runs the concierge in interactive mode but injects some initial dummy information, which should behave like "Riccardo is flying to London next Tuesday for a single day, pick all the other info from etc/sample-family.yaml".

## Testing

It's hard to test a long-running job. try never to reproduce running a long-running job.
If you have to, make sure to prepend a "timeout 10 <command>" to ensure you fail after 10sec.
This should help catch compile and other initial errors.
