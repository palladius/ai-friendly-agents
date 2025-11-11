# Workshop Travel Agent ✈️🏨🧳

> **Status:** 🚧 Work In Progress (v0.2.x) 🚧

Welcome to the **Workshop Travel Agent**, a multi-agent AI concierge built with the [Google Agent Development Kit (ADK)](https://github.com/google/adk-python). This application uses a team of specialized AI agents to help you plan your perfect trip.

## 🤖 Meet the Team

*   🎩 **Androsthenes (Concierge):** Your primary contact and trip manager. He orchestrates the entire planning process, understands your family's preferences, and ensures a smooth experience by coordinating the specialized agents below.
    *   ✈️ **Fabio Volo (Flights):** The flight specialist. He finds the best routes and deals for your journey.
    *   🛏️ **Barabba (Hotels):** The accommodation expert. He searches for hotels and Airbnbs that match your needs.
    *   🗺️ *Antiochus (Itinerary): [Planned] The destination connoisseur. He crafts personalized daily itineraries and recommends local experiences.*
    *   💰 *Scrooge (Budget): [Planned] The finance manager. He keeps track of costs to ensure your trip stays within budget.*

## 🚀 Features (Current)

*   **Interactive Concierge:** Chat with Androsthenes to plan your trip.
*   **Personalization:** Reads family profiles from `etc/sample-family.yaml` to know who's traveling.
*   **Multi-Agent Coordination:** The Concierge delegates tasks to Flight and Hotel agents.
*   **Real-time Awareness:** Agents can use tools like `now()` to understand the current context.
*   **MCP Integration (WIP):** Integrating with Model Context Protocol (MCP) servers for real-world data (e.g., Airbnb for hotels).

## 🛠️ Usage

This project uses `uv` for dependency management and `just` for command execution.

### Quick Start

Run the interactive concierge:

```bash
just run
```

### Testing

Run the unit test suite:

```bash
just test
```

Test the Hotel agent in isolation (using Airbnb MCP):

```bash
just run-hotel-agent
```

Run a specific end-to-end test scenario:

```bash
just run-concierge-testing-hotel-agent
```

## 📂 Project Structure

*   `src/`: Source code for agents and tools.
*   `tests/`: Unit and integration tests.
*   `etc/`: Configuration files (e.g., family profiles).
*   `PLAN.md`: Development roadmap and milestones.