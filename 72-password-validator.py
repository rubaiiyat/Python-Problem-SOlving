password = "Aaaa3geGeq"


cnt = 0
num = 0
up = 0
low = 0
for i in range(len(password)):
    cnt += 1
    val = ord(password[i])

    if val >= 65 and val <= 90:
        up += 1

    if val >= 97 and val <= 122:
        low += 1

    if val >= 48 and val <= 57:
        num += 1


if cnt >= 8 and num >= 1 and up >= 1 and low >= 1:
    print("Valid Password")
else:
    print("Not Valid Password")
