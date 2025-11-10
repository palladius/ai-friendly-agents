from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Person:
    Name: str
    Surname: str
    Role: str
    DOB: str
    PassPort: str
    Interests: List[str]
    Nationality: Optional[str] = None

@dataclass
class Address:
    Street: str
    City: str
    Country: str
    ZipCode: str

@dataclass
class TravelProps:
    TravellerType: str
    PreferredAirlines: List[str]
    HotelPreferences: List[str]
    DietaryRestrictions: List[str]
    SpecialNeeds: List[str]

@dataclass
class Budget:
    TotalBudget: str
    BudgetFlexibility: str
    Days: int
    MealPerPerson: str
    AccommodationPerNight: str

    def __post_init__(self):
        self.TotalBudget = int(self.TotalBudget.split()[0])
        self.MealPerPerson = int(self.MealPerPerson.split()[0])
        self.AccommodationPerNight = int(self.AccommodationPerNight.split()[0])

@dataclass
class Family:
    Family: List[Person]
    Address: Address
    TravelProps: TravelProps
    Budget: Budget
