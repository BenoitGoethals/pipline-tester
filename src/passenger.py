class Passenger:
    MINIMUM_AGE = 12
    VALID_GENDERS = {"male", "female"}
    ERROR_EMPTY_NAME = "Name cannot be an empty string."
    ERROR_AGE_TOO_LOW = f"Passengers must be at least {MINIMUM_AGE} years old."
    ERROR_INVALID_GENDER = "Gender must be either male or female."

    def __init__(self, *, name, age, gender):
        self.name = name  # Triggers name validation via setter
        self.age = age  # Triggers age validation via setter
        self.gender = gender  # Triggers gender validation via setter

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(self.ERROR_EMPTY_NAME)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MINIMUM_AGE:
            raise ValueError(self.ERROR_AGE_TOO_LOW)
        self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value not in self.VALID_GENDERS:
            raise ValueError(self.ERROR_INVALID_GENDER)
        self.__gender = value



    def __str__(self):
        return f"{self.name} of age {self.age} is a {self.gender}."

    def __repr__(self):
        return f"Passenger({self.name}, {self.age}, {self.gender})"








