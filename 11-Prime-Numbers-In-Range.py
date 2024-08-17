start = 25
end = 50

middle = end // 2

for num in range(start, end + 1):
    for i in range(2, middle + 1):
        if (num % i) == 0:
            break
    else:
        print(num)
