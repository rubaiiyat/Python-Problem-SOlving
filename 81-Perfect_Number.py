n = int(input())

while n > 0:
    num = int(input())

    mid = num // 2
    sum = 0
    flag = 0
    for i in range(mid + 1):
        sum += i

        if sum == num:
            print(num, "eh perfeito")
            break

    else:
        print(num, "nao eh perfeito")

    n -= 1
