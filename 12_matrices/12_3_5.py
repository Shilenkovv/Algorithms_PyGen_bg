def reshape(matrix: list[list[int]], row: int, col: int) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])

    new_mat = [[0] * col for _ in range(row)]
    elem_num = 0
    for i in range(n):
        for j in range(m):
            new_mat[elem_num // col][elem_num % col] = matrix[i][j]
            elem_num += 1

    return new_mat


matrix = [[1, 2, 3], [4, 5, 6]]

reshaped_matrix = reshape(matrix, 1, 6)
print(*reshaped_matrix, sep='\n')

matrix = [[1, 2, 3], [4, 5, 6]]

reshaped_matrix = reshape(matrix, 3, 2)
print(*reshaped_matrix, sep='\n')
