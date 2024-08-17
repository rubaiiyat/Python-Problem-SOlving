num = 5

count = 0
for i in range(1, num + 1):
    val = "2" * i
    print(val, end=" + ")
    count += int(val)
print("Total sum:", count)
