class Vehicle:
    def __init__(self, name, mileage, speed) -> None:
        self.name = name
        self.mileage = mileage
        self.speed = speed


class Bus(Vehicle):
    pass


bus = Bus("Ena", 500, 200)
print(type(bus))
