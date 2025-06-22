def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # if i == j:
            #     matrix[i][j] = 0
            if i < j:
                matrix[i][j] = 1
            elif i > j:
                matrix[i][j] = 2

    return matrix


matrix = create_matrix(5)
print(*matrix, sep='\n')
