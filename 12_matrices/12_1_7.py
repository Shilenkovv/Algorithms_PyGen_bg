def min_below_secondary_diagonal(matrix: list[list[int]]) -> int:
    n = len(matrix)
    min_elem = float('inf')

    for i in range(n):
        for j in range(n):
            if i + j >= n:
                min_elem = min(min_elem, matrix[i][j])
    return min_elem
