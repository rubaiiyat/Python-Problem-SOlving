def merge_sort(arr):
    l = len(arr)

    if l <= 1:
        return arr

    mid = l // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


arr = [6, 3, 7, 1, 2, 5, 9, 20, 32, 12, 32, 23, 54, 45, 65, 56, 76, 14, 32]
print(arr)
srt = merge_sort(arr)
print(srt)
