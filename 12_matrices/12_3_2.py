def winner(matrix: list[list[str]]) -> str:
    from collections import defaultdict

    field = defaultdict(set)
    for i in range(3):
        field['main_d'].add(matrix[i][i])
        field['second_d'].add(matrix[i][2 - i])
        field['0-'].add(matrix[0][i])
        field['1-'].add(matrix[1][i])
        field['2-'].add(matrix[2][i])
        field['-0'].add(matrix[i][0])
        field['-1'].add(matrix[i][1])
        field['-2'].add(matrix[i][2])

    for v in field.values():
        if len(v) == 1:
            if 'X' in v:
                return 'X'
            elif 'O' in v:
                return 'O'
    return 'Draw'


# game_area = [['O', '-', 'X'], ['-', 'X', '-'], ['X', '-', 'O']]

# print(winner(game_area))  # X

# game_area = [['X', 'O', 'X'], ['O', 'O', 'O'], ['-', 'X', 'X']]

# print(winner(game_area))  # O

# game_area = [['X', 'O', '-'], ['-', 'X', '-'], ['-', 'O', 'X']]

# print(winner(game_area))  # X

# game_area = [['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]

# print(winner(game_area))  # Draw
