import logging
from google.adk.agents import LlmAgent
from google.adk.sessions import Session
from src.tools import get_default_travel_dates, calculate_date, now
from src.data_classes import Family
from src.flight_agent import FlightAgent
from src.hotel_agent import HotelAgent
from typing import List
from pydantic import PrivateAttr

class ConciergeAgent(LlmAgent):
    _logger: logging.Logger = PrivateAttr()

    def __init__(self, name: str, model: str, family_config: Family, log_file: str = None):
        super().__init__(
            name=name,
            model=model,
            instruction=f"""Welcome! You are a helpful concierge agent. Your main task is to greet the user and assist with their travel plans.
            
            IMPORTANT RULE: You have a `calculate_date` tool. When the user mentions a relative date like 'today', 'tomorrow', or 'in 3 days', you MUST use the `calculate_date` tool to determine the absolute date before calling any other agent's tools. Do not ask the user for the date.
            
            Start by saluting the first person in the family list, {family_config.Family[0].Name}.
            You are assisting the {family_config.Family[0].Surname} family. The family consists of:
            {', '.join([f'{p.Name} ({p.Role})' for p in family_config.Family])}.
            
            Propose a default travel plan for 2 adults, from Milan to Sal, Capo Verde, using the `get_default_travel_dates()` tool to get the dates.
            
            If the user asks for flight information, delegate the task to the `Fabio_Volo` agent.
            If the user asks for hotel information, delegate the task to the `Barabba` agent.
            """,
            description="A concierge agent that greets users, proposes a default travel plan, and delegates flight and hotel queries.",
            tools=[get_default_travel_dates, calculate_date, now],
            sub_agents=[
                FlightAgent(name="Fabio_Volo", model=model, log_file="log/flight_agent.log"),
                HotelAgent(name="Barabba", model=model, log_file="log/hotel_agent.log")
            ]
        )
        self._logger = logging.getLogger(self.name)
        if log_file is None:
            log_file = f"log/{self.name}.log"
        handler = logging.FileHandler(log_file, mode="w")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)
        self._logger.info(f"Initializing ConciergeAgent with name: {self.name}")

    async def run(self, session: Session):
        # Proactively get the current date and add it to the session state
        current_date = now().split(" ")[0] # Get just the date part
        session.context["current_date"] = current_date
        self._logger.info(f"Proactively set current_date to: {current_date}")

        # Make the current_date available to the tools
        self.tools["calculate_date"].keywords["current_date"] = current_date
        self.tools["get_default_travel_dates"].keywords["current_date"] = current_date

        await super().run(session)
