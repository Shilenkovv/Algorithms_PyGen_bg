def is_diagonally_dominant(matrix: list[list[int]]) -> bool:
    n = len(matrix)

    for i in range(n):
        row_sum = 0
        for j in range(n):
            if i != j:
                row_sum += abs(matrix[i][j])
        if abs(matrix[i][i]) < row_sum:
            return False
    return True


# matrix = [[3, -2, 1], [1, -3, 2], [-1, 2, 4]]

# print(is_diagonally_dominant(matrix))  # True

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(is_diagonally_dominant(matrix))  # False
