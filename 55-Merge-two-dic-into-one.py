dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}

# dict3 = {**dict1, **dict2}

dict3 = dict()
l = len(dict1) if len(dict2) >= len(dict1) else len(dict2)

for item, value in dict1.items():
    dict3[item] = value
for item, value in dict2.items():
    dict3[item] = value
print(dict3)
