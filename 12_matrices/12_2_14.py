def create_matrix(n: int) -> list[list[int]]:
    matrix = [[1] * n for _ in range(n)]
    zero_idx = 1

    while zero_idx < n:
        for i in range(zero_idx, n):
            matrix[zero_idx][i] = 0
            matrix[i][zero_idx] = 0
        zero_idx += 2

    return matrix


# matrix = create_matrix(1, 1)
# print(*matrix, sep='\n')

matrix = create_matrix(5)
print(*matrix, sep='\n')
