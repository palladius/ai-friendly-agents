import yaml
from .data_classes import Family, Person, Address, TravelProps, Budget

def load_config(path: str) -> Family:
    """Loads a YAML configuration file and returns a Family object."""
    with open(path, "r") as f:
        config_data = yaml.safe_load(f)
    
    family_members = [Person(**member) for member in config_data["Family"]]
    address = Address(**config_data["Address"])
    travel_props = TravelProps(**config_data["TravelProps"])
    budget = Budget(**config_data["Budget"])

    return Family(
        Family=family_members,
        Address=address,
        TravelProps=travel_props,
        Budget=budget
    )
