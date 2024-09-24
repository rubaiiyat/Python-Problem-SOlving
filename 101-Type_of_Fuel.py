a = 0
g = 0
d = 0

while True:
    x = int(input())

    if x == 4:
        break

    if x == 1:
        a += 1
    elif x == 2:
        g += 1
    elif x == 3:
        d += 1
    else:
        continue

print("MUITO OBRIGADO")
print("Alcool:", a)
print("Gasolina:", g)
print("Diesel:", d)
