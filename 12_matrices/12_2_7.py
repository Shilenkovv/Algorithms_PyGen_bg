def create_matrix(n: int, m: int) -> list[list[int]]:
    matrix = [[0] * m for _ in range(n)]
    cur_elem = 1

    for j in range(m):
        for i in range(n):
            matrix[i][j] = cur_elem
            cur_elem += 1

    return matrix


matrix = create_matrix(3, 5)
print(*matrix, sep='\n')
