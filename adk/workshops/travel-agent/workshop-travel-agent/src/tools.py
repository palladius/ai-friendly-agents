from datetime import datetime, timedelta

def now() -> str:
    """Returns the current date and time in a human-readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_default_travel_dates() -> str:
    """Calculates the date of the next Saturday and the Saturday after that."""
    today = datetime.now()
    days_until_saturday = (5 - today.weekday() + 7) % 7
    next_saturday = today + timedelta(days=days_until_saturday)
    saturday_after = next_saturday + timedelta(weeks=1)
    return f"from {next_saturday.strftime('%Y-%m-%d')} to {saturday_after.strftime('%Y-%m-%d')}"
