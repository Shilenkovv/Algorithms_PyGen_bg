def count_columns(matrix: list[list[int]], target: int) -> int:
    n = len(matrix)
    m = len(matrix[0])

    targ_count = 0

    for j in range(m):
        for i in range(n):
            if matrix[i][j] == target:
                targ_count += 1
                break

    return targ_count


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(count_columns(data, 5))  # 1

data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

print(count_columns(data, 1))  # 3

data = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print(count_columns(data, 4))  # 0
