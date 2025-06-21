def row_with_min_sum(matrix: list[list[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    row_min_sum = float('inf')

    for i in range(n):
        row_sum = 0
        for j in range(m):
            row_sum += matrix[i][j]
        if row_sum <= row_min_sum:
            row_min_sum = row_sum
            row_min_num = i
    return row_min_num


# matrix = [[1, 5, 3], [2, 8, 6], [5, 9, 3], [8, 6, 0]]

# print(row_with_min_sum(matrix))  # 0

# matrix = [[5, 9, 3], [5, 9, 3], [5, 9, 3], [5, 9, 3]]

# print(row_with_min_sum(matrix))  # 3

# matrix = [[1]]

# print(row_with_min_sum(matrix))  # 0
