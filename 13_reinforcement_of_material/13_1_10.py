from typing import List


def matrix_search(matrix: List[List[int]], target: int) -> bool:
    n, m = len(matrix), len(matrix[0])

    i, j = 0, m - 1
    while i < n and j >= 0:
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target and matrix[i][0] <= target:
            j -= 1
        elif matrix[i][j] == target:
            return True
        else:
            return False
    return False


# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# print(matrix_search(matrix, 11))  # True

# matrix = [[-33, -12, 89], [45, 77, 100]]

# print(matrix_search(matrix, 77))  # True


# matrix = [[14, 16, 55], [20, 20, 67], [23, 67, 88]]

# print(matrix_search(matrix, 1))  # False

# matrix = [[2]]

# print(matrix_search(matrix, 2))  # True

# matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

# print(matrix_search(matrix, -1))  # False


# matrix = [
#     [3, 7, 9, 10, 13],
#     [16, 17, 17, 21, 21],
#     [24, 24, 25, 28, 28],
#     [28, 31, 32, 33, 36],
#     [38, 41, 41, 42, 42],
#     [45, 45, 47, 50, 50],
#     [51, 53, 57, 57, 60],
#     [61, 63, 66, 69, 69],
# ]
# print(matrix_search(matrix, 61))
