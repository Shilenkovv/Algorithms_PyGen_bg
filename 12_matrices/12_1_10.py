def sum_edge_elements(matrix: list[list[int]]) -> int:
    n = len(matrix)
    ans = 0

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                ans += matrix[i][j]
    return ans


# matrix = [[3, 6, -8, 5], [1, -2, 7, -4], [-5, -10, 0, -3], [-10, -2, -2, 5]]

# print(sum_edge_elements(matrix))  # -14
