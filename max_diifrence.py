def merge(arr, l, m, r):
    """
    Merge two subarrays of arr[].

    Args:
    - arr (list): The input list to be sorted.
    - l (int): Left index of the first subarray.
    - m (int): Middle index of the first subarray.
    - r (int): Right index of the second subarray.
    """
    n1 = m - l + 1
    n2 = r - m

    # Create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    """
    Main function that sorts arr[] using merge().

    Args:
    - arr (list): The input list to be sorted.
    - l (int): Left index of the subarray to be sorted.
    - r (int): Right index of the subarray to be sorted.
    """
    if l < r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
print("array : ", arr)


def partition_array(arr):
    """
    Partition the sorted array into two subarrays and calculate the maximum difference between their sums.

    Args:
    - arr (list): The input list to be partitioned.

    Returns:
    - sum_left (int): The sum of elements in the left subarray.
    - sum_right (int): The sum of elements in the right subarray.
    - arr (list): The sorted input list.
    - left_array (list): The left subarray.
    - right_array (list): The right subarray.
    """
    n = len(arr)
    mergeSort(arr, 0, n - 1)
    n_2 = int(n / 2)
    right_array = arr[n_2:n]
    left_array = arr[0:n_2]

    sum_left = 0
    sum_right = 0
    for i in range(len(left_array)):
        sum_left += left_array[i]

    for i in range(len(right_array)):
        sum_right += right_array[i]

    return sum_left, sum_right, arr, left_array, right_array


sum_left, sum_right, arr, left_array, right_array = partition_array(arr)

print("sorted array : ", arr)
print("right sub array : ", right_array)
print("left sub array : ", left_array)
print("max difference : ", abs(sum_left - sum_right))
