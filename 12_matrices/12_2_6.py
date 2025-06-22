def create_matrix(n: int, m: int, k: int) -> list[list[int]]:
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i + j == k:
                matrix[i][j] = 1

    return matrix


# matrix = create_matrix(4)
# print(*matrix, sep='\n')
