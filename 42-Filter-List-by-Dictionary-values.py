roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97}

lst = []

for i in range(len(roll_number)):

    for item, val in sample_dict.items():
        if val == roll_number[i]:
            lst.append(val)

print(lst)
