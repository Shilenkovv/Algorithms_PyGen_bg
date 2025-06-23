def count_sorted_rows(matrix: list[list[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    if m == 1:
        return n
    ans = 0

    for i in range(n):
        is_asc = False
        if matrix[i][1] > matrix[i][0]:
            is_asc = True
        for j in range(1, m):
            if is_asc:
                if matrix[i][j] <= matrix[i][j - 1]:
                    break
            else:
                if matrix[i][j] >= matrix[i][j - 1]:
                    break
        else:
            ans += 1
    return ans


# matrix = [[1, 1, 1], [2, 5, 4], [1, 2, 0], [3, 8, 1]]

# print(count_sorted_rows(matrix))  # 0

# matrix = [[1, 2, 3], [6, 5, 4], [7, 7, 7], [7, 8, 9]]

# print(count_sorted_rows(matrix))  # 3
