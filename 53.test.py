def quicksort(A, start, end):
    if start < end:
        # Partition the array and get the pivot index
        p = partition(A, start, end)
        # Recursively sort elements before and after the pivot
        quicksort(A, start, p - 1)
        quicksort(A, p + 1, end)


def partition(A, start, end):
    pivot = A[start]  # The pivot is the first element
    i = start + 1  # Start from the second element

    # Iterate through the array from start+1 to end
    for j in range(start + 1, end + 1):
        if A[j] < pivot:
            # Swap elements smaller than the pivot
            A[i], A[j] = A[j], A[i]
            i += 1  # Increment index for smaller elements

    # Place the pivot in its correct position
    A[start], A[i - 1] = A[i - 1], A[start]

    return i - 1  # Return the new index of the pivot


# Example usage
arr = [6, 3, 7, 1, 2, 5, 9, 20, 32, 12, 32, 23, 54, 45, 65, 56, 76, 14, 32]
print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
