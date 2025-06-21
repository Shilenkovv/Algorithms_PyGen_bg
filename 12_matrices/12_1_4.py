def max_on_main_diagonal(matrix: list[list[int]]) -> int:
    n = len(matrix)
    max_elem = -float('inf')

    for i in range(n):
        for j in range(n):
            if i == j:
                max_elem = max(max_elem, matrix[i][j])

    return max_elem
