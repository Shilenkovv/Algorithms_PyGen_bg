def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    elem = 1

    for start in range(n):
        i, j = 0, start

        while i < n and j < n:
            matrix[i][j] = elem
            i += 1
            j += 1
            elem += 1

    return matrix


# matrix = create_matrix(5)
# print(*matrix, sep='\n')
