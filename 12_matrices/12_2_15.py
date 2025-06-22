def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        fill_value = (i + 1) % 2
        for j in range(n):
            matrix[i][j] = (fill_value) % 2
            fill_value += 1

    return matrix


# matrix = create_matrix(1, 1)
# print(*matrix, sep='\n')

matrix = create_matrix(4)
print(*matrix, sep='\n')
