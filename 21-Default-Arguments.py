def defaultValue(name, salary=9000):
    return f"Name: {name}\nSalary: {salary}"


defVal = defaultValue("Daniel", 12000)
print(defVal)
defVal = defaultValue("Ava")
print(defVal)
