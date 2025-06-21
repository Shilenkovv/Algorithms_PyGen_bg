def sum_shaded_area(matrix: list[list[int]]) -> int:
    n = len(matrix)
    ans = 0

    for i in range(n):
        for j in range(n):
            if (i < j and i < n - 1 - j) or (i > j and i > n - 1 - j):
                ans += matrix[i][j]

    return ans


# matrix = [[-10, 1, 6], [1, 5, -3], [6, -3, 3]]

# print(is_symmetric(matrix))  # True

# matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

# print(is_symmetric(matrix))  # True

# matrix = [[1, 2], [3, 4]]

# print(is_symmetric(matrix))  # False
