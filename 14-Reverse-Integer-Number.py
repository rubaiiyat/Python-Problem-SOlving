num = 76542

while num > 0:
    newNum = num
    newNum %= 10
    num //= 10
    print(newNum, end="")
