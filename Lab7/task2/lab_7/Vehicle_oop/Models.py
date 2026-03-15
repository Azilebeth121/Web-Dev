class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model}'s engine started."

    def stop_engine(self):
        return f"{self.brand} {self.model}'s engine stopped."

    def move(self):
        return "The vehicle is moving."

    def __str__(self):
        return f"Vehicle: {self.brand} {self.model} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def move(self):  
        return f"The car {self.brand} {self.model} is driving on the road."

    def honk(self):
        return "Beep beep!"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def move(self):  
        return f"The motorcycle {self.brand} {self.model} is speeding on the highway."

    def wheelie(self):
        return "The motorcycle performs a wheelie!"