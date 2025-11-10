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

def calculate_date(relative_date: str) -> str:
    """Calculates an absolute date from a relative date string.
    
    Args:
        relative_date: The relative date string (e.g., "tomorrow", "in 3 days").
    
    Returns:
        The absolute date in YYYY-MM-DD format.
    """
    today = datetime.now()
    if "tomorrow" in relative_date.lower():
        return (today + timedelta(days=1)).strftime("%Y-%m-%d")
    elif "in" in relative_date.lower() and "days" in relative_date.lower():
        try:
            days = int(relative_date.split("in")[1].split("days")[0].strip())
            return (today + timedelta(days=days)).strftime("%Y-%m-%d")
        except ValueError:
            return "Invalid date format"
    else:
        return "Unsupported relative date"
