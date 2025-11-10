import logging
from google.adk.agents import LlmAgent
from src.tools import now, get_default_travel_dates
from src.data_classes import Family, FlightData, HotelData
from src.flight_agent import FlightAgent
from src.hotel_agent import HotelAgent
from typing import List

class ConciergeAgent(LlmAgent):
    def __init__(self, name: str, model: str, family_config: Family, flight_data: List[FlightData], hotel_data: List[HotelData]):
        logging.info(f"Initializing ConciergeAgent with name: {name}")
        flight_agent = FlightAgent(name="Fabio_Volo", model=model, flight_data=flight_data)
        hotel_agent = HotelAgent(name="Barabba", model=model, hotel_data=hotel_data)
        super().__init__(
            name=name,
            model=model,
            instruction=f"""Welcome! You are a helpful concierge agent. Your main task is to greet the user and confirm their travel details.
            Start by saluting the first person in the family list, {family_config.Family[0].Name}.
            Use the `now()` tool to get the current date and time and include it in your greeting.
            You are assisting the {family_config.Family[0].Surname} family. The family consists of:
            {', '.join([f'{p.Name} ({p.Role})' for p in family_config.Family])}.
            Their preferred travel type is '{family_config.TravelProps.TravellerType}'.
            Their budget flexibility is '{family_config.Budget.BudgetFlexibility}'.
            
            Propose a default travel plan for 2 adults, from Milan to Sal, Capo Verde, using the `get_default_travel_dates()` tool to get the dates.
            
            If the user asks for flight information, delegate the task to the `Fabio_Volo` agent.
            If the user asks for hotel information, delegate the task to the `Barabba` agent.
            """,
            description="A concierge agent that greets users, proposes a default travel plan, and delegates flight and hotel queries.",
            tools=[now, get_default_travel_dates],
            sub_agents=[flight_agent, hotel_agent]
        )

# Example usage (for testing purposes, not part of the agent definition itself)
if __name__ == "__main__":
    # This part would typically be in a runner or main application file
    concierge = ConciergeAgent(name="Androsthenes", model="gemini-2.5-flash")
    print(f"Concierge Agent Name: {concierge.name}")
    print(f"Concierge Agent Description: {concierge.description}")
