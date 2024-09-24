a = 0
b = 1
li = [0, 1]


for i in range(61):
    c = a + b
    li.append(c)

    a = b
    b = c


n = int(input())

for i in range(n):
    m = int(input())

    print(f"Fib({m}) = {li[m]}")
