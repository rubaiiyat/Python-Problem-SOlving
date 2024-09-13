arr = [3, 5, 6, 8, 14, 17, 28, 35, 60, 100]
length = len(arr)
beg = 0
end = length - 1
item = 2

while end >= beg:
    mid = (beg + end) // 2

    if arr[mid] == item:
        print(mid)
        break
    elif item > arr[mid]:
        beg = mid + 1
    else:
        end = mid - 1

else:
    print("Not Found")
