def sum_middle_row_and_column(matrix: list[list[int]]) -> int:
    mid_idx = len(matrix) // 2
    n = len(matrix)

    tot = 0

    for i in range(n):
        tot += matrix[mid_idx][i]
        tot += matrix[i][mid_idx]

    return tot - matrix[mid_idx][mid_idx]


# game_area = [['O', '-', 'X'], ['-', 'X', '-'], ['X', '-', 'O']]

# print(winner(game_area))  # X

# game_area = [['X', 'O', 'X'], ['O', 'O', 'O'], ['-', 'X', 'X']]

# print(winner(game_area))  # O

# game_area = [['X', 'O', '-'], ['-', 'X', '-'], ['-', 'O', 'X']]

# print(winner(game_area))  # X

# game_area = [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]

# print(winner(game_area))  # Draw
