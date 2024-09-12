a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]

l = len(a)
item = 1
beg = 0
end = l - 1

for i in range(l):
    mid = (beg + end) // 2
    if mid == item:
        print(i)
        break
    elif item < mid:
        l = mid - 1
    elif item > mid:
        beg = mid + 1
else:
    print("Not Found")
