n = int(input())

for i in range(n):
    text = input().lower().split()

    if "thor" in text:
        print("Y")
    else:
        print("N")
