class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f"Name: {self.name},Max Speed: {self.max_speed},Mileage: {self.mileage}"


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


bus = Bus("Ford Mustang", 500, 100)
print(bus)
