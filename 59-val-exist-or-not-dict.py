sample_dict = {"a": 100, "b": 200, "c": 300}

val = 200

for item, value in sample_dict.items():
    if val == value:
        print(val, "present in a dict")
        break


else:
    print(val, "is not present in dict")
