from airplane import Airplane
from passenger import Passenger


def main():
    print("Hello from pipline-tester!")
    airplane = Airplane(name="Airplane 1",capacity=50)
    airplane.add_passenger(Passenger(name="ben",age=55,gender="male"))
    airplane.add_passenger(Passenger(name="john",age=25,gender="male"))
    airplane.add_passenger(Passenger(name="jane",age=35,gender="female"))
    airplane.add_passenger(Passenger(name="michael",age=45,gender="male"))

    print(airplane.get_capacity_left())
    for passenger in airplane.passengers:
        print(passenger.name)



if __name__ == "__main__":
    main()
