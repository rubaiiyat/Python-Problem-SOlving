class Vehicle:
    color = "Black"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f"Name: {self.name} and Color: {self.color}"


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


bus = Bus("Ena", 500, 100)
print(bus)
car = Bus("Toyota", 600, 200)
print(car)
