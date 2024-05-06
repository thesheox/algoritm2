def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

arr = [12, 11, 13, 5, 6, 7]
print("array : ", arr)
def partition_array(arr):
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
