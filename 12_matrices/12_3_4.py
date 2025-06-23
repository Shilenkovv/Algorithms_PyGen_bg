def count_special_positions(matrix: list[list[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    speical_pos = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                cur_sum = 0
                for k in range(n):
                    cur_sum += matrix[k][j]
                for k in range(m):
                    cur_sum += matrix[i][k]
                if cur_sum == 2:
                    speical_pos += 1

    return speical_pos


matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

print(count_special_positions(matrix))
