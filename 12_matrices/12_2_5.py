def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix


# matrix = create_matrix(4)
# print(*matrix, sep='\n')
