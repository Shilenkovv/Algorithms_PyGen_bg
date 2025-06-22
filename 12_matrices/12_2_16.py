def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    fill_value = 1
    start_row = len(matrix) - 1

    while fill_value <= n:
        for i in range(start_row, -1, -1):
            matrix[start_row][i + (n - 1 - start_row)] = fill_value
            matrix[i][n - 1 - start_row] = fill_value
        fill_value += 1
        start_row -= 1

    return matrix


# matrix = create_matrix(1, 1)
# print(*matrix, sep='\n')

matrix = create_matrix(5)
print(*matrix, sep='\n')
