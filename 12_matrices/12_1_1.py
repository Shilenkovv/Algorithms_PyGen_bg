def diagonal_sum(matrix: list[list[int]]) -> int:
    ans = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j or i + j == len(matrix) - 1:
                ans += matrix[i][j]
    return ans


# matrix = [[8, 8, 2, 10], [9, 1, 6, 7], [4, 6, 1, 7], [3, 10, 0, 9]]

# print(diagonal_sum(matrix))
