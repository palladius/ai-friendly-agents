import logging
from google.adk.agents import LlmAgent
from src.data_classes import FlightData
from typing import List

class FlightAgent(LlmAgent):
    def __init__(self, name: str, model: str, flight_data: List[FlightData]):
        logging.info(f"Initializing FlightAgent with name: {name}")
        super().__init__(
            name=name,
            model=model,
            instruction="You are a flight agent. Your main task is to find flights based on a given destination.",
            description="A flight agent that finds flights from a list of available flights.",
            tools=[self.search_flights]
        )
        self._flight_data = flight_data

    def search_flights(self, destination: str) -> List[dict]:
        """Searches for flights to a given destination."""
        logging.info(f"Searching for flights to: {destination}")
        for data in self._flight_data:
            if data.destination.lower() == destination.lower():
                logging.info(f"Found flights to: {destination}")
                return [flight.__dict__ for flight in data.flights]
        logging.info(f"No flights found to: {destination}")
        return []
