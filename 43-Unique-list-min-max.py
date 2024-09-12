sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

unique_list = []

for item in sample_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
print(min(unique_list))
print(max(unique_list))
