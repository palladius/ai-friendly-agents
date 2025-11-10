import unittest
import asyncio
from src.flight_agent import FlightAgent
from src.config import load_flight_data

class TestFlightAgent(unittest.TestCase):
    def setUp(self):
        self.flight_data = load_flight_data("etc/sample-flight.yaml")

    def test_search_flights(self):
        """Tests that the flight agent can find flights to a given destination."""
        agent = FlightAgent(name="TestFlightAgent", model="gemini-2.5-flash", flight_data=self.flight_data)
        flights = agent.search_flights("Sal, Capo Verde")
        self.assertEqual(len(flights), 2)
        self.assertEqual(flights[0]["airline"], "TAP Air Portugal")

    def test_search_flights_not_found(self):
        """Tests that the flight agent returns an empty list when no flights are found."""
        agent = FlightAgent(name="TestFlightAgent", model="gemini-2.5-flash", flight_data=self.flight_data)
        flights = agent.search_flights("Nonexistent Destination")
        self.assertEqual(len(flights), 0)

if __name__ == "__main__":
    unittest.main()
