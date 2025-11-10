
## First prompt

```markdown
Help me create an ADK travel multi-agent in **python** and `uvx` framework for virtualenv'ing. We will call it "workshop-travel-agent".

I'd like to have the following:
1. A `Concierge` who asks the user the dates when they want to travel (default being: 2 adults, next saturday to the saturday afterwards from Milan to Sal, Capo Verde). Concierge is in charge with User requests, particularly budget, flexibility on dates, and so on.
2. A `travel agent` is in charge with knowing what's nice to do in the destination,
   best season, what do you need to prep in advance, and so on. It might just say "I recommend AGAINST flying during this season as its monsoon season". So it takes into input the proposed dates and stuff, checks weather and stuff, and builds it.
2. A `Hotel agent` who uses AirBNB MCP server https://github.com/openbnb-org/mcp-server-airbnb to search for B&Bs. Ideally the hotel agent
3. A `flight agent` who uses google this MCP to search for flights: https://github.com/salamentic/google-flights-mcp
4. A `budget agent` will try to understand the costs, and try to delineate a budget in tabular form, assuming a certain amount per day for food. Default: `30$` per meal per person. He will also deal with currency change and propose in the local currency (default: `EUR`).

The flow will have to offer a final output in HTML/PDF and have:
1. flight details, transport from airport/hotel, ..
2. Ideally these agents should be able to have some STATE/MEMORY (eg, `travel agent` suggests the best CITY where it makes sense to sleep, and the `hotel_agent` looks for B&Bs in that particular location).

For simplicity, the person should be able to provide a YAML of preferences, where they tell you:
1. Array of Name, Surname, Passports.
2. Type of traveller: chill out by the pool vs travel all around every day with no rest
3. Budget: how much for food (eg 30$ per meal), how much for hotel (eg 200$/night/couple), total budget and flexibility on budget: strict vs ballpark.

The flow will have to be semi-parallel, with the Flight agent first deciding the EXACT dates, then the hotel agent can do the second part. Finally the Travel agent, knowing where person is sleeping, can arrange a day-by-day travel plan.

The final output will be a HTML/PDF and a version number (eg `Zurich___Mykonos_YYYYMMDD_HHMMSS_Plan01.html`) and can be amended and perfected over time. Of course, you can also talk to the agent tomorrow, update your previous HTML/PDF and ask for an amendment => `Zurich___Mykonos_YYYYMMDD_HHMMSS_Plan02.html`

Since this is a complex task, always start with a PLAN.md and divide it in Milestones.
For instance, for v1.0 we can skip Budget and Travel Agent, and just do Flights and configuration from `etc/my-family.yaml`
```
