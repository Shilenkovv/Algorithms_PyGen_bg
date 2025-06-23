def has_common_element_in_rows(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    m = len(matrix[0])

    total_rows_set = set()

    for i in range(n):
        row_set = set()
        for j in range(m):
            row_set.add(matrix[i][j])
        if i == 0:
            total_rows_set = row_set
        else:
            total_rows_set = total_rows_set.intersection(row_set)
            if len(total_rows_set) == 0:
                return False
    return True


matrix = [[1, 2, 3], [3, 4, 5], [2, 3, 4]]

print(has_common_element_in_rows(matrix))
