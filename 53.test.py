def merge_sort(array):
    # Base case: If the array has 1 or no elements, it is already sorted
    if len(array) <= 1:
        return array

    # Find the middle point and divide the array into two halves
    middle = len(array) // 2
    left_half = merge_sort(array[:middle])
    right_half = merge_sort(array[middle:])

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []  # Resultant array
    left_index = 0
    right_index = 0

    # Merge while both arrays have elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left array
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # Append any remaining elements from the right array
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_array = merge_sort(arr)
print("Sorted array:", sorted_array)
