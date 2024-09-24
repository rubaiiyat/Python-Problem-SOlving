while True:
    try:
        a, b = list(map(int, input().split()))

        c = a - b
        print(abs(c))
    except EOFError:
        break
