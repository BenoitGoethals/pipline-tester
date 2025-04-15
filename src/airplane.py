from passenger import Passenger


class Airplane:
    def __init__(self, *,name, capacity):
        self.__name = name
        self.__capacity = capacity
        self.__passengers:list[Passenger] = []


    @property
    def name(self):
        return self.__name

    @property
    def capacity(self):
        return self.__capacity

    @property
    def passengers(self):
        return self.__passengers

    def get_capacity_left(self):
        return self.__capacity - len(self.__passengers)

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        self.__name = value


    def add_passenger(self, passen:Passenger,):
        if self.get_capacity_left() == 0:
            raise Exception("Not enough capacity.")
        self.__passengers.append(passen)

