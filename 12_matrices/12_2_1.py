def create_matrix(n: int, m: int) -> list[list[int]]:
    row = [0] * m
    for j in range(m):
        row[j] = j
    matrix = [row] * n

    return matrix


# matrix = create_matrix(3, 4)
# print(*matrix, sep='\n')
