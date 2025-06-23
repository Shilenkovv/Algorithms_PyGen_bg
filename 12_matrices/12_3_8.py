def fill_ones(matrix: list[list[int]]) -> None:
    from collections import defaultdict

    n = len(matrix)
    m = len(matrix[0])

    rows_ones = defaultdict(int)
    cols_ones = defaultdict(int)

    for i in range(n):
        for j in range(m):
            rows_ones[i] += matrix[i][j]
            cols_ones[j] += matrix[j][i]

    for i in range(n):
        for j in range(m):
            if rows_ones[i] != 0 or cols_ones[j] != 0:
                matrix[i][j] = 1


matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

fill_ones(matrix)
print(*matrix, sep='\n')
