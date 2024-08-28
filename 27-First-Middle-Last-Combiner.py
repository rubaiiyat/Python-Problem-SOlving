s1 = input()
s2 = input()

l1 = len(s1)
l2 = len(s2)

m1 = l1 // 2
m2 = l2 // 2

print(s1[0] + s2[0] + s1[m1] + s2[m2] + s1[l1 - 1] + s2[l2 - 1])
