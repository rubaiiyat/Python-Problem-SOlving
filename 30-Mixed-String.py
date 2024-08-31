s1 = "Abc"
s2 = "Xyz"
s3 = ""
length = len(s1) if len(s1) > len(s2) else len(s2)
s2 = s2[::-1]
for i in range(length):
    s3 += s1[i]
    s3 += s2[i]


print(s3)
