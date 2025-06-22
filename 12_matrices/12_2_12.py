def create_matrix(n: int, m: int) -> list[list[int]]:
    matrix = [[0] * m for _ in range(n)]
    mat_shape = n * m
    cur_elem = 1
    i = 0
    j = 0

    while cur_elem <= mat_shape:
        while i < n:
            matrix[i][j] = cur_elem
            cur_elem += 1
            i += 1
        j += 1
        i = n - 1
        if cur_elem >= mat_shape:
            break
        while i >= 0:
            matrix[i][j] = cur_elem
            cur_elem += 1
            i -= 1
        j += 1
        i = 0

    return matrix


# matrix = create_matrix(1, 1)
# print(*matrix, sep='\n')

# matrix = create_matrix(3, 5)
# print(*matrix, sep='\n')
