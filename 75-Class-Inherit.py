class Vehicle:
    def __init__(self, name, max_speed, mileage) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=50) -> None:
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def __str__(self) -> str:
        return f"Name: {self.name} and Seat Capacity {self.capacity} passengers"


bus = Bus("Ena", 500, 100)

print(bus)
