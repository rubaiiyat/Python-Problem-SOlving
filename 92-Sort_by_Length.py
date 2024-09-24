n = int(input())

for _ in range(n):
    text = input().split()

    rev = sorted(text, key=len, reverse=True)

    print(" ".join(rev))
