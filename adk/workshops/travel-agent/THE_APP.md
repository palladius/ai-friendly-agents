
Help me create an ADK travel multi-agent called "workshop-travel-agent" and nicknamed Androsthenes of Cyzicus (a great traveller, and in italian "Androstene di Kúzikos" => AdK).

I'd like to have the following:
1. A `Concierge` ("Androsthenes") who asks the user the dates when they want to travel (default being: 2 adults, next saturday to the saturday afterwards from Milan to Sal, Capo Verde). Concierge is in charge with User requests, particularly budget, flexibility on dates, and so on. Concierge should be able to:
   1. know what time and date it is (create a function for it: `now()` )
   2. Read a config file (for now we consider it just prompt text. A future version might have pydantic validation)
   3. The concierge agent can be called with "-f/--file <path/to/file>" which allows it to know your family and travel tastes. This should be tested with the `etc/sample-family.yaml` file.
2. A `travel agent` ("Antiochus") is in charge with knowing what's nice to do in the destination,
   best season, what do you need to prep in advance, and so on. It might just say "I recommend AGAINST flying during this season as its monsoon season". So it takes into input the proposed dates and stuff, checks weather and stuff, and builds it.
3. A `Hotel agent` ("Barabba") who uses AirBNB MCP server https://github.com/openbnb-org/mcp-server-airbnb to search for B&Bs. Ideally the hotel agent
4. A `flight agent` ("Fabio Volo") who uses google this MCP to search for flights: https://github.com/salamentic/google-flights-mcp
5. A `budget agent` ("Scrooge") will try to understand the costs, and try to delineate a budget in tabular form, assuming a certain amount per day for food. Default: `30$` per meal per person. He will also deal with currency change and propose in the local currency (default: `EUR`).

The flow will have to offer a final output in HTML/PDF and have:
1. flight details, transport from airport/hotel, ..
2. Ideally these agents should be able to have some STATE/MEMORY (eg, `travel agent` suggests the best CITY where it makes sense to sleep, and the `hotel_agent` looks for B&Bs in that particular location).

For simplicity, the person should be able to provide a YAML of preferences, where they tell you:
1. Array of Name, Surname, Passports.
2. Type of traveller: chill out by the pool vs travel all around every day with no rest
3. Budget: how much for food (eg 30$ per meal), how much for hotel (eg 200$/night/couple), total budget and flexibility on budget: strict vs ballpark.

The flow will have to be semi-parallel, with the Flight agent first deciding the EXACT dates, then the hotel agent can do the second part. Finally the Travel agent, knowing where person is sleeping, can arrange a day-by-day travel plan.

The final output will be a HTML/PDF and a version number (eg `Zurich___Mykonos_YYYYMMDD_HHMMSS_Plan01.html`) and can be amended and perfected over time. Of course, you can also talk to the agent tomorrow, update your previous HTML/PDF and ask for an amendment => `Zurich___Mykonos_YYYYMMDD_HHMMSS_Plan02.html`

## Config

A config file is under `etc/sample-family.yaml`. Note that this info can be overridden.
For example, a family of four could have a trip organized for one of them plus a fifth,
or some budget can be overridden for work, and so on.
