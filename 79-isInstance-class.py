class Vehicle:
    def __init__(self, name, mileage, speed, capacity) -> None:
        self.name = name
        self.mileage = mileage
        self.speed = speed
        self.capacity = capacity


class Bus(Vehicle):
    pass


bus = Bus("Hanif", 500, 200, 50)

print(isinstance(bus, Vehicle))
