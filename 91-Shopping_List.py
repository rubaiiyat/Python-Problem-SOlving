n = int(input())

for i in range(n):
    text = input().split()

    unique_text = sorted(set(text))

    print(" ".join(unique_text))
