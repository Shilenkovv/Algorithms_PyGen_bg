def create_matrix(n: int) -> list[list[int]]:
    matrix = [[4] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                matrix[i][j] = 0
            elif i < j:
                if i < n - 1 - j:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 2
            elif i > j:
                if i > n - 1 - j:
                    matrix[i][j] = 3

    return matrix


# matrix = create_matrix(2)
# print(*matrix, sep='\n')
