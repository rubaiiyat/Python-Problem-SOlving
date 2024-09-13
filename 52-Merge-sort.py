def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add the remaining elements from both halves
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


# Test the merge_sort function
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
