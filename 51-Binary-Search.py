a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]

l = len(a)
item = 15
beg = 0
end = l - 1

while beg <= end:
    mid = (beg + end) // 2
    if a[mid] == item:
        print(mid)
        break
    elif item < a[mid]:
        end = mid - 1
    elif item > a[mid]:
        beg = mid + 1
else:
    print("Not Found")
