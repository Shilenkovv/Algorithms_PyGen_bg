def create_matrix(n: int, m: int) -> list[list[int]]:
    matrix = [[1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i % 2 and j % 2:
                matrix[i][j] = 0
    return matrix
