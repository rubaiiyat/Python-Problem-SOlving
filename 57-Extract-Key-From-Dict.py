sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

for val, key in sample_dict.items():
    if val == keys[0]:
        print(key)

    if val == keys[1]:
        print(key)
