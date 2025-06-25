def winner(game_area: list[list[str]]) -> str:
    from collections import defaultdict

    rows_dict = defaultdict(set)
    cols_dict = defaultdict(set)
    main_d = set()
    second_d = set()

    n = len(game_area)
    for i in range(n):
        for j in range(n):
            if i == j:
                main_d.add(game_area[i][j])
            if i + j == n - 1:
                second_d.add(game_area[i][j])
            rows_dict[i].add(game_area[i][j])
            cols_dict[j].add(game_area[i][j])

    if main_d == set('X') or second_d == set('X'):
        return 'X'
    elif main_d == set('O') or second_d == set('O'):
        return 'O'
    for dict_iter in [rows_dict, cols_dict]:
        for v in dict_iter.values():
            if len(v) == 1:
                if 'X' in v:
                    return 'X'
                elif 'O' in v:
                    return 'O'
    return 'Draw'


# game_area = [['X', 'O', '-'], ['-', 'X', '-'], ['-', 'O', 'X']]

# print(winner(game_area))
