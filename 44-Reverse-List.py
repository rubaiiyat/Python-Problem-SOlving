list1 = [100, 200, 300, 400, 500]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i], end=" ")
print()
list1.reverse()
print(list1)
