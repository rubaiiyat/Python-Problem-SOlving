def quickSort(a, start, end):
    if start < end:
        p = partition(a, start, end)
        quickSort(a, start, p - 1)
        quickSort(a, p + 1, end)


def partition(a, start, end):
    pivot = a[start]
    i = start + 1

    for j in range(start + 1, end + 1):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[start], a[i - 1] = a[i - 1], a[start]
    return i - 1


arr = [6, 3, 7, 1, 2, 5, 9, 20, 32, 12, 32, 23, 54, 45, 65, 56, 76, 14, 32]
print(arr)
quickSort(arr, 0, len(arr) - 1)
print(arr)
