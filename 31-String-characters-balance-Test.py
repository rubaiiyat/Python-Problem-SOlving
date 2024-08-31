s1 = "Ynf"
s2 = "PYnative"


length = len(s2)

flag = False

for char in s1:
    if char in s2:
        flag = True
    else:
        flag = False

print(flag)
