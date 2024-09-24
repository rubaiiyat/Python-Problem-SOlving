while True:
    try:
        a, b = list(map(int, input().split()))

        fact1 = 1
        fact2 = 1
        for i in range(1, a + 1):
            fact1 *= i

        for i in range(1, b + 1):
            fact2 *= i

        print(fact1 + fact2)

    except EOFError:
        break
