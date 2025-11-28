## WORKSHOP_PLAN.md

After talking to my friend Maurizio Ipsale, the path is clear. Here is my overall plan.

1. Take some simple things from my `complex-travel-agent/` and downport them to my `simple-travel-agent/`.

This workshop should have the following steps:

1. **Basic working copy**. Copy basic agent functionalities for a possibly in YAML format, which is simple and beautiful.
2. **Add now() tool**. Show it fails at solving a simple thing like: "Book a hotel in Milan for today and tomorrow", since it doesn't know what day is it today. => suggest people to create a tool.
   1. This might be commented code, with non-implemented function, or function implemented as `{status: success, value: YOUR_CODE_HERE .. }`
3. **Add GoogleSearch() tool**. Now chat with ADK and ask it to find a hotel. Again -> fake hotels, .. no success.
   1. Add the *Google Search* tool.
   2. Now test it again -> it should work. Yay!
4. **Enter MCP**. Problem: Now we should ask to find hotels with certain aspects, like price, area, ..
   1. It should NOT work great.
   2. Introduce MCP client to Airbnb.
5. **Milestone 1: it works!**. Test end2end. This should be the end of it.
   1. People should be able to test it a bit.


## Additional steps

These can be done in order, or not, based on people preferences:

1. [HARd] Add memory: memorize user name, surname, passport number, preferences.
2. [MEDIUM] Deploy to Cloud Run and/or to Vertex AI. And then integrate with `Gemini enterprise`, why not?
3. [Easy] Add file writing tools (copy idea from `complex-travel-agent/`)
4. [Easy] Add a mocked function to do `PlaceID` lookup for AirBNB. Airbnb supports fine graid search for PlaceID, but they're hard to find. For instance:
   1. "Milano Isola" PlaceID: `ChIJ1bQ-cy3BhkcRFhYVJNHBZuY`.
   2. "Place de la Madeleine Geneva". Place ID: `Ei5QbC4gZGUgbGEgTWFkZWxlaW5lLCAxMjA0IEdlbsOodmUsIFN3aXR6ZXJsYW5kIi4qLAoUChIJSRXC1i1ljEcRuFYl7aGWyzcSFAoSCevi0JMGZYxHETm8C3s1lbag`
   3. We could just have a sample extensible array in a etc/place_ids.yaml where the tool is able to do a lookup. finder online is here: https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder

