def create_matrix(n: int) -> list[list[int]]:
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j or i + j == n - 1:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    return matrix


# matrix = create_matrix(5)
# print(*matrix, sep='\n')
