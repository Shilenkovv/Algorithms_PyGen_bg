def print_matrix_diagonally(matrix: list[list[int]]) -> None:
    n = len(matrix)

    for start in range(n):
        i, j = start, 0
        cur_list = []
        while i >= 0 and j < n:
            cur_list.append(matrix[i][j])
            i -= 1
            j += 1
        print(' '.join(map(lambda x: str(x), cur_list)))

    for start in range(1, n):
        i, j = n - 1, start
        cur_list = []
        while i >= 0 and j < n:
            cur_list.append(matrix[i][j])
            i -= 1
            j += 1
        print(' '.join(map(lambda x: str(x), cur_list)))
    return True


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print_matrix_diagonally(matrix)
