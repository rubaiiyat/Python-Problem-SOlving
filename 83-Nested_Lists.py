n = int(input())

li = []
while n > 0:
    name = input()
    score = float(input())

    li.append([name, score])

    n -= 1


sort_num = sorted(set(num for name, num in li))

mn = sort_num[1]

nam = []
for name, num in li:
    if mn == num:
        nam.append(name)

nam.sort()

for n in nam:
    print(n)


""" for n, i in li:
    print(max(i)) """
