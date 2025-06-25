def is_symmetric(matrix: list[list[int]]) -> str:
    n = len(matrix)

    is_vert_symm = True
    is_hor_symm = True

    for i in range(n):
        for j in range(n):
            if is_vert_symm and matrix[i][j] != matrix[i][n - 1 - j]:
                is_vert_symm = False
            if is_hor_symm and matrix[i][j] != matrix[n - 1 - i][j]:
                is_hor_symm = False
            if not is_hor_symm and not is_vert_symm:
                return 'no'

    if is_hor_symm and is_vert_symm:
        return 'both'
    elif is_vert_symm:
        return 'vertical'
    return 'horizontal'


matrix = [[1, 2, 3], [4, 4, 4], [1, 2, 3]]

print(is_symmetric(matrix))  # horizontal

matrix = [[1, 4, 1], [2, 4, 2], [3, 4, 3]]

print(is_symmetric(matrix))  # vertical

matrix = [[1, 2, 1], [2, 2, 2], [1, 2, 1]]

print(is_symmetric(matrix))  # both

matrix = [[1]]

print(is_symmetric(matrix))  # both

matrix = [[1, -2, -2, 6], [8, 5, 5, 8], [9, 5, 5, 9], [-8, -3, -3, 1]]

print(is_symmetric(matrix))  # no
