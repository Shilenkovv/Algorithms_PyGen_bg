def print_matrix_with_reversed_rows(matrix: list[list[int]]) -> None:
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m - 1, -1, -1):
            print(matrix[i][j], end=' ')
        print()


matrix = [[3, 2, 1, 0], [6, 5, 4, 10], [9, 8, 7, 15]]

print_matrix_with_reversed_rows(matrix)
