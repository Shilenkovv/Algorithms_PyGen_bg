def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    ones_idx = 0

    while ones_idx <= n // 2 + 1:
        for i in range(ones_idx, n - ones_idx):
            matrix[i][ones_idx] = 1
            matrix[ones_idx][i] = 1
            matrix[n - 1 - ones_idx][i] = 1
            matrix[i][n - 1 - ones_idx] = 1
        ones_idx += 2
    return matrix


# matrix = create_matrix(1, 1)
# print(*matrix, sep='\n')

matrix = create_matrix(10)
print(*matrix, sep='\n')
