def is_special(matrix: list[list[int]]) -> bool:
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                if matrix[i][j] == 0:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True
