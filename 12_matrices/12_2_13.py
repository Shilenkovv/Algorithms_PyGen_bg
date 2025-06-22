def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if n - 2 <= i + j <= n:
                matrix[i][j] = 1

    return matrix


# matrix = create_matrix(1, 1)
# print(*matrix, sep='\n')

# matrix = create_matrix(4)
# print(*matrix, sep='\n')
