class Vehicle:
    def __init__(self, name, mileage, capacity) -> None:
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fareAm(self):
        return self.capacity * 100

    def __str__(self) -> str:
        return f"Name: {self.name}, Mileage: {self.mileage}, Capacity: {self.capacity}"


class Bus(Vehicle):
    def fare(self):
        amount = super().fareAm()
        total = self.capacity * 10
        totalAmout = amount + total

        return totalAmout


bus = Bus("Ena", 12, 50)
print(bus)
print("Total Amount:", bus.fare())
