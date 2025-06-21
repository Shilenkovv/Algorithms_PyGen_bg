def is_magic_square(matrix: list[list[int]]) -> bool:
    n = len(matrix)

    main_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - i - 1]

    if main_diagonal_sum != secondary_diagonal_sum:
        return False

    for i in range(n):
        row_sum = 0
        col_sum = 0
        for j in range(n):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]

        if not row_sum == col_sum == main_diagonal_sum:
            return False

    return True


# matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

# print(is_magic_square(matrix))
