from typing import List


def winner(matrix: List[List[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    rows_max = {row_num: -float('inf') for row_num in range(n)}
    rows_sum = {row_num: 0 for row_num in range(n)}

    for i in range(n):
        cur_sum = 0
        for j in range(m):
            rows_max[i] = max(rows_max[i], matrix[i][j])
            cur_sum += matrix[i][j]
        rows_sum[i] = cur_sum

    winner_number = 0

    for k in rows_max:
        if rows_max[k] > rows_max[winner_number]:
            winner_number = k
        elif rows_max[k] == rows_max[winner_number]:
            if rows_sum[k] > rows_sum[winner_number]:
                winner_number = k

    return winner_number


# scores = [[3, 3, 2], [6, 6, 8], [5, 3, 4], [6, 5, 4]]

# print(winner(scores))  # 1

# scores = [[5, 6, 5], [6, 5, 8], [8, 6, 7], [3, 5, 4]]

# print(winner(scores))  # 2

# scores = [[7, 6, 6], [6, 7, 6], [2, 2, 4], [5, 4, 3]]

# print(winner(scores))  # 0

# scores = [[5]]

# print(winner(scores))  # 0
