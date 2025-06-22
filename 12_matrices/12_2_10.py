def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]

    for start in range(n):
        i, j = 0, start
        cur_elem = j + 1
        while i < n and j < n:
            matrix[i][j] = cur_elem
            i += 1
            j += 1

    for start in range(1, n):
        i, j = start, 0
        cur_elem = i + 1
        while i < n and j < n:
            matrix[i][j] = cur_elem
            i += 1
            j += 1

    return matrix


matrix = create_matrix(5)
print(*matrix, sep='\n')
