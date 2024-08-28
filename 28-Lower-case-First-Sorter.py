str1 = input()

""" for s in str1:
    if s >= "a" and s <= "z":
        print(s, end="")

for s in str1:
    if s >= "A" and s <= "Z":
        print(s, end="") """


low = []
up = []

for s in str1:
    if s >= "a" and s <= "z":
        low.append(s)
    else:
        up.append(s)

print("".join(low + up))
