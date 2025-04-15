# File: tests/test_airplane.py

import pytest
from src.airplane import Airplane
from src.passenger import Passenger


def test_airplane_initialization():
    airplane = Airplane(name="Boeing 747", capacity=300)
    assert airplane.name == "Boeing 747"
    assert airplane.capacity == 300
    assert airplane.passengers == []


def test_airplane_invalid_name():
    airplane = Airplane(name="Boeing 747", capacity=300)
    with pytest.raises(ValueError, match="Name cannot be an empty string."):
        airplane.name = ""


def test_airplane_get_capacity_left_empty():
    airplane = Airplane(name="Boeing 747", capacity=300)
    assert airplane.get_capacity_left() == 300


def test_airplane_get_capacity_left_with_passengers():
    airplane = Airplane(name="Boeing 747", capacity=2)
    passenger1 = Passenger(name="Alice", age=30, gender="female")
    passenger2 = Passenger(name="Bob", age=35, gender="male")
    airplane.add_passenger(passenger1)
    airplane.add_passenger(passenger2)
    assert airplane.get_capacity_left() == 0


def test_add_passenger_success():
    airplane = Airplane(name="Boeing 747", capacity=2)
    passenger = Passenger(name="John Doe", age=25, gender="male")
    airplane.add_passenger(passenger)
    assert len(airplane.passengers) == 1
    assert airplane.passengers[0] == passenger


def test_add_passenger_exceeds_capacity():
    airplane = Airplane(name="Boeing 747", capacity=1)
    passenger1 = Passenger(name="Alice", age=30, gender="female")
    passenger2 = Passenger(name="Bob", age=35, gender="male")
    airplane.add_passenger(passenger1)
    with pytest.raises(Exception, match="Not enough capacity."):
        airplane.add_passenger(passenger2)
