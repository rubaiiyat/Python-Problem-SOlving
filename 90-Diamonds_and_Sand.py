n = int(input())


for i in range(n):
    line = input().strip()
    cnt = 0
    stack = []

    for char in line:
        if char == "<":
            stack.append("<")
        elif char == ">":
            if stack:
                stack.pop()
                cnt += 1

    print(cnt)
