import yaml
from typing import List
from .data_classes import Family, Person, Address, TravelProps, Budget, Flight, FlightData, Hotel, HotelData

def load_flight_data(path: str) -> List[FlightData]:
    """Loads a YAML flight data file and returns a list of FlightData objects."""
    with open(path, "r") as f:
        flight_data = yaml.safe_load(f)
    
    return [
        FlightData(
            destination=data["destination"],
            flights=[Flight(**flight) for flight in data["flights"]]
        )
        for data in flight_data
    ]

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

def load_hotel_data(path: str) -> List[HotelData]:
    """Loads a YAML hotel data file and returns a list of HotelData objects."""
    with open(path, "r") as f:
        hotel_data = yaml.safe_load(f)
    
    return [
        HotelData(
            destination=data["destination"],
            hotels=[Hotel(**hotel) for hotel in data["hotels"]]
        )
        for data in hotel_data
    ]
