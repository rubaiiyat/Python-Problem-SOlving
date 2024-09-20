class car:

    name = ""
    color = ""

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color


tesla = car("Tesla Model S", "Red")

print(tesla.name)
print(tesla.color)
