def create_matrix(n: int, m: int) -> list[list[int]]:
    matrix = [[1] * m for _ in range(n)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i % 2 and j % 2:
                matrix[i][j] = 0
    return matrix


matrix = create_matrix(5, 6)
print(*matrix, sep='\n')
