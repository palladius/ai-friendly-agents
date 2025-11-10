from google.adk.agents import LlmAgent

class ConciergeAgent(LlmAgent):
    def __init__(self, name: str, model: str):
        super().__init__(
            name=name,
            model=model,
            instruction="Welcome! You are a helpful concierge agent. Your main task is to greet the user and confirm their travel details.",
            description="A concierge agent that greets users and gathers initial travel information."
        )

# Example usage (for testing purposes, not part of the agent definition itself)
if __name__ == "__main__":
    # This part would typically be in a runner or main application file
    concierge = ConciergeAgent(name="Androsthenes", model="gemini-2.5-flash")
    print(f"Concierge Agent Name: {concierge.name}")
    print(f"Concierge Agent Description: {concierge.description}")
