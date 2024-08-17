numbers = [12, 75, 150, 180, 200, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    if num % 5 == 0:
        print(num)
