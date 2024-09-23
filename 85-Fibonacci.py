n = 10

a = 0
b = 1

for i in range(3, n + 1):
    c = a + b
    print(c, end=" ")

    a = b
    b = c
