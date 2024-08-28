str1 = "P@#yn26at^&i5ve"

charCnt = 0
digitCnt = 0
symbolCnt = 0

""" for s in str1:
    myascii = ord(s)
    if (myascii >= 65 and myascii <= 90) or (myascii >= 97 and myascii <= 122):
        charCnt += 1
    elif myascii >= 48 and myascii <= 57:
        digitCnt += 1
    else:

        symbolCnt += 1 """

for s in str1:
    if s.isalpha():
        charCnt += 1
    elif s.isdigit():
        digitCnt += 1
    else:
        symbolCnt += 1

print("Char:", charCnt)
print("Digit:", digitCnt)
print("Symbol:", symbolCnt)
