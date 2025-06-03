def sum_in_rectangles(matrix: list[list[int]], rectangles: list[list[tuple[int]]]) -> list[int]:
    n = len(matrix)
    m = len(matrix[0])
    pre_mat = [[0 for _ in range(m + 1)] for _ in range(n)]
    for i in range(n):
        for j in range(1, m + 1):
            pre_mat[i][j] = pre_mat[i][j - 1] + matrix[i][j - 1]

    ans = []

    for coords in rectangles:
        row1, col1 = coords[0]
        row2, col2 = coords[1]
        cur_sum = 0
        for i in range(row1, row2 + 1):
            cur_sum += pre_mat[i][col2 + 1] - pre_mat[i][col1]
        ans.append(cur_sum)
    return ans


# matrix = [[-1, 0, -3], [2, 5, -10], [-1, 2, 0]]
# rectangles = [[(0, 0), (2, 2)], [(0, 1), (1, 2)]]
# print(sum_in_rectangles(matrix, rectangles))

# matrix = [[9, 4, 1], [2, 5, 0], [4, 2, 8]]
# rectangles = [[(0, 0), (1, 1)], [(1, 0), (2, 2)]]

# print(sum_in_rectangles(matrix, rectangles))

# matrix = [[1, 2], [3, 3]]
# rectangles = [[(0, 0), (1, 1)]]

# print(sum_in_rectangles(matrix, rectangles))

# matrix = [[10, -2], [9, -9], [-4, 0]]
# rectangles = [[(1, 0), (2, 1)], [(2, 1), (2, 1)], [(2, 0), (2, 0)]]
# print(sum_in_rectangles(matrix, rectangles))

# matrix = [[7, -5], [-4, 3]]
# rectangles = [[(1, 1), (1, 1)], [(1, 1), (1, 1)], [(0, 1), (1, 1)]]
# print(sum_in_rectangles(matrix, rectangles))
