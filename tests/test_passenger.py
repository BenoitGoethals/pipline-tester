import pytest

from src.passenger import Passenger


def test_passenger_initialization():
    passenger = Passenger(name="John Doe", age=25, gender="male")
    assert passenger.name == "John Doe"
    assert passenger.age == 25
    assert passenger.gender == "male"


def test_passenger_name_validation():
    with pytest.raises(ValueError) as excinfo:
        Passenger(name="", age=25, gender="male")
    assert str(excinfo.value) == Passenger.ERROR_EMPTY_NAME


def test_passenger_age_validation():
    with pytest.raises(ValueError) as excinfo:
        Passenger(name="John Doe", age=10, gender="male")
    assert str(excinfo.value) == Passenger.ERROR_AGE_TOO_LOW


def test_passenger_gender_validation():
    with pytest.raises(ValueError) as excinfo:
        Passenger(name="John Doe", age=25, gender="other")
    assert str(excinfo.value) == Passenger.ERROR_INVALID_GENDER


def test_passenger_str_representation():
    passenger = Passenger(name="John Doe", age=25, gender="male")
    assert str(passenger) == "John Doe of age 25 is a male."


def test_passenger_repr_representation():
    passenger = Passenger(name="John Doe", age=25, gender="male")
    assert repr(passenger) == "Passenger(John Doe, 25, male)"
