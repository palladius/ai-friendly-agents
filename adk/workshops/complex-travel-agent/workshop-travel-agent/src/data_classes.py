from dataclasses import dataclass
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class HotelSearchQuery(BaseModel):
    location: str
    checkin: Optional[date] = None
    checkout: Optional[date] = None
    adults: Optional[int] = 1
    children: Optional[int] = 0
    infants: Optional[int] = 0
    maxPrice: Optional[int] = None

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

@dataclass
class Flight:
    airline: str
    flight_number: str
    departure_airport: str
    arrival_airport: str
    departure_time: str
    arrival_time: str
    duration: str
    price: str

@dataclass
class FlightData:
    destination: str
    flights: List[Flight]

@dataclass
class Hotel:
    name: str
    rating: float
    price_per_night: str
    amenities: List[str]

@dataclass
class HotelData:
    destination: str
    hotels: List[Hotel]
