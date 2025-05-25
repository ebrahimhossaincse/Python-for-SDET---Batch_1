class Vehicle:
    _brand = "Test Vehicle"
    brand2= "Test Vehicle"
    def __init__(self, model, year):
        self._model = model # protected
        self._year = year

class Car(Vehicle):
    def __init__(self, model, year, speed):
        super().__init__(model, year)
        self._speed = speed

    def display(self):
        print(f"Model: {self._model}, Year: {self._year}, Speed: {self._speed}, {self._brand}")

car = Car("Honda", 2020, 160)
car.display()
