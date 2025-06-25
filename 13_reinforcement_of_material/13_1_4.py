def sum_diagonal_extremes(matrix: list[list[int]]) -> int:
    n = len(matrix)
    max_elem_main_d = -float('inf')
    min_elem_second_d = float('inf')

    for i in range(n):
        max_elem_main_d = max(max_elem_main_d, matrix[i][i])
        min_elem_second_d = min(min_elem_second_d, matrix[i][n - 1 - i])

    return max_elem_main_d + min_elem_second_d


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(sum_diagonal_extremes(matrix))
