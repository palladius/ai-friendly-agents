import unittest
import asyncio
from src.hotel_agent import HotelAgent
from src.config import load_hotel_data

class TestHotelAgent(unittest.TestCase):
    def setUp(self):
        self.hotel_data = load_hotel_data("etc/sample-hotel.yaml")

    def test_search_hotels(self):
        """Tests that the hotel agent can find hotels in a given destination."""
        agent = HotelAgent(name="TestHotelAgent", model="gemini-2.5-flash", hotel_data=self.hotel_data)
        hotels = agent.search_hotels("Sal, Capo Verde")
        self.assertEqual(len(hotels), 2)
        self.assertEqual(hotels[0]["name"], "Hilton Sal")

    def test_search_hotels_not_found(self):
        """Tests that the hotel agent returns an empty list when no hotels are found."""
        agent = HotelAgent(name="TestHotelAgent", model="gemini-2.5-flash", hotel_data=self.hotel_data)
        hotels = agent.search_hotels("Nonexistent Destination")
        self.assertEqual(len(hotels), 0)

if __name__ == "__main__":
    unittest.main()
