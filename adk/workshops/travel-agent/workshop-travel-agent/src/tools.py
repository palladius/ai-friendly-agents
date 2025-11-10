from datetime import datetime

def now() -> str:
    """Returns the current date and time in a human-readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
