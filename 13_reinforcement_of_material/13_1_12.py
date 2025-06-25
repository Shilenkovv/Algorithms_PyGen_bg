from typing import List


def saddle_points(matrix: List[List[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    rows_min = {row_num: float('inf') for row_num in range(n)}
    cols_max = {col_num: -float('inf') for col_num in range(m)}

    for i in range(n):
        for j in range(m):
            rows_min[i] = min(rows_min[i], matrix[i][j])
            cols_max[j] = max(cols_max[j], matrix[i][j])

    ans = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == rows_min[i] == cols_max[j]:
                ans += 1
    return ans


# matrix = [[1, 2], [3, 4]]

# print(saddle_points(matrix))  # 1

# matrix = [[2, 6], [3, 1]]

# print(saddle_points(matrix))  # 0

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(saddle_points(matrix))  # 1

# matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

# print(saddle_points(matrix))  # 9

# matrix = [[1], [2], [3]]

# print(saddle_points(matrix))  # 1
