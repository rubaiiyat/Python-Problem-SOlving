def recur(n):

    if n == 1:
        return 1
    else:
        return n + recur(n - 1)


print(recur(10))
