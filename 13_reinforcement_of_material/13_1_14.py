from typing import List


def count_columns_with_max(matrix: List[List[int]]) -> int:
    n = len(matrix)
    max_elem = -float('inf')
    ans = 0

    for i in range(n):
        for j in range(n):
            max_elem = max(max_elem, matrix[i][j])

    for j in range(n):
        for i in range(n):
            if matrix[i][j] == max_elem:
                ans += 1
                break

    return ans


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(count_columns_with_max(matrix))  # максимум (9) содержится только в третьем столбце # 1
