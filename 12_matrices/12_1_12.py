def modify_by_average(matrix: list[list[int]]) -> None:
    n = len(matrix)
    m = len(matrix[0])

    tot_sum = 0
    for i in range(n):
        for j in range(m):
            tot_sum += matrix[i][j]
    tot_avg = tot_sum / (n * m)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] < tot_avg:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1


# matrix = [[3, 2, 1, 0], [6, 5, 4, 10], [9, 8, 7, 15]]

# modify_by_average(matrix)
# print(*matrix)
