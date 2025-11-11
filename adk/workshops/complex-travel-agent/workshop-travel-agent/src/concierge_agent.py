import logging
from google.adk.agents import LlmAgent
from src.tools import get_default_travel_dates, calculate_date
from src.lib.file_tools import write_plan, list_plans, read_plan
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
            instruction=f"""Your most important rule is to use the `calculate_date` tool whenever a user mentions a relative date. You MUST NOT ask the user for the date. For example, if the user says 'tomorrow', you must call `calculate_date(relative_date='tomorrow')`.
            
            You are a helpful concierge agent. Your main task is to greet the user and assist with their travel plans.
            
            You have the following tools to manage travel plans:
            - `write_plan`: to save a travel plan to disk.
            - `list_plans`: to list existing travel plans.
            - `read_plan`: to read a travel plan from a file.

            When writing a plan, you MUST follow these formatting rules:
            - Use tables for multiple choices.
            - Always start with a synoptic overview.
            - Use hyperlinks for all references.
            - Be concise: prefer a linked title over a title and a separate link.
            
            Start by saluting the first person in the family list, {family_config.Family[0].Name}.
            You are assisting the {family_config.Family[0].Surname} family. The family consists of:
            {', '.join([f'{p.Name} ({p.Role})' for p in family_config.Family])}.
            
            After greeting the user, you MUST propose a default travel plan for 2 adults, from Milan to Sal, Capo Verde, using the `get_default_travel_dates()` tool to get the dates.
            
            If the user asks for flight information, delegate the task to the `Fabio_Volo` agent.
            if the user asks for hotel information, delegate the task to the `Barabba` agent.
            """,
            description="A concierge agent that greets users, proposes a default travel plan, and delegates flight and hotel queries.",
            tools=[get_default_travel_dates, calculate_date, write_plan, list_plans, read_plan],
            sub_agents=[
                FlightAgent(name="Fabio_Volo", model=model, log_file="log/flight_agent.log"),
                HotelAgent(name="Barabba", model=model, log_file="log/hotel_agent.log")
            ]
        )
        self._logger = logging.getLogger(self.name)
        if log_file is None:
            log_file = f"log/{self.name}.log"
        handler = logging.FileHandler(log_file, mode="a")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)
        self._logger.info(f"Initializing ConciergeAgent with name: {self.name}")
