import logging
from google.adk.agents import LlmAgent
from src.data_classes import HotelData
from typing import List

class HotelAgent(LlmAgent):
    def __init__(self, name: str, model: str, hotel_data: List[HotelData]):
        logging.info(f"Initializing HotelAgent with name: {name}")
        super().__init__(
            name=name,
            model=model,
            instruction="You are a hotel agent. Your main task is to find hotels based on a given destination.",
            description="A hotel agent that finds hotels from a list of available hotels.",
            tools=[self.search_hotels]
        )
        self._hotel_data = hotel_data

    def search_hotels(self, destination: str) -> List[dict]:
        """Searches for hotels in a given destination."""
        logging.info(f"Searching for hotels in: {destination}")
        for data in self._hotel_data:
            if data.destination.lower() == destination.lower():
                logging.info(f"Found hotels in: {destination}")
                return [hotel.__dict__ for hotel in data.hotels]
        logging.info(f"No hotels found in: {destination}")
        return []
