list1 = [34, 54, 67, 89, 11, 43, 94]

print(list1)

index = 4
item = list1[index]
list1.pop(index)
print(f"List After removing element at index {index}: ", list1)

list1.insert(2, item)
print("List after Adding element at index 2: ", list1)

list1.append(item)
print("List after Adding element at last: ", list1)
