from google.adk.agents import LlmAgent
from src.tools import now
from src.data_classes import Family

class ConciergeAgent(LlmAgent):
    def __init__(self, name: str, model: str, family_config: Family):
        super().__init__(
            name=name,
            model=model,
            instruction=f"""Welcome! You are a helpful concierge agent. Your main task is to greet the user and confirm their travel details.
            The current date and time is {{now()}}.
            You are assisting the {family_config.Family[0].Surname} family. The family consists of:
            {', '.join([f'{p.Name} ({p.Role})' for p in family_config.Family])}.
            Their preferred travel type is '{family_config.TravelProps.TravellerType}'.
            Their budget flexibility is '{family_config.Budget.BudgetFlexibility}'.
            """,
            description="A concierge agent that greets users, gathers initial travel information, and uses the current date/time and family preferences.",
            tools=[now]
        )

# Example usage (for testing purposes, not part of the agent definition itself)
if __name__ == "__main__":
    # This part would typically be in a runner or main application file
    concierge = ConciergeAgent(name="Androsthenes", model="gemini-2.5-flash")
    print(f"Concierge Agent Name: {concierge.name}")
    print(f"Concierge Agent Description: {concierge.description}")
