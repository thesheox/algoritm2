def search_recursive(matrix, target, row, col):
    # Base case: If row index exceeds matrix length or column index goes below zero, return False
    if row >= len(matrix) or col < 0:
        return False

    # If current element equals target, return True
    if matrix[row][col] == target:
        return True
    # If current element is less than target, move down in the matrix
    elif matrix[row][col] < target:
        return search_recursive(matrix, target, row + 1, col)  # Move down
    # If current element is greater than target, move left in the matrix
    else:
        return search_recursive(matrix, target, row, col - 1)  # Move left

def search_in_sorted_matrix(matrix, target):
    # If matrix is empty, return False
    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Start searching from the top-right corner of the matrix
    return search_recursive(matrix, target, 0, cols - 1)

# Example usage:
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17],
]

target = 13
print(search_in_sorted_matrix(matrix, target))  # Output: True

target = 15
print(search_in_sorted_matrix(matrix, target))  # Output: False
