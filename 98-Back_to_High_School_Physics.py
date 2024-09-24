while True:
    try:
        a, b = list(map(int, input().split()))

        print(a * 2 * b)

    except EOFError:
        break


