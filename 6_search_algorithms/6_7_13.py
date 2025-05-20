def matrix_search(matrix: list[list[int]], target: int) -> bool:
    if matrix[0][0] > target or matrix[-1][-1] < target:
        return False
    cur_row = 0
    while cur_row <= (len(matrix) - 1):
        if target > matrix[cur_row][-1]:
            cur_row += 1
            continue
        elif target < matrix[cur_row][0]:
            return False
        else:
            left, right = 0, len(matrix[cur_row]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                elem = matrix[cur_row][mid]
                if elem == target:
                    return True
                elif elem < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
    return False


# data = [[-10, -9, -8], [-7, -6, -5], [-4, -3, -2]]

# print(matrix_search(data, -2))

# data = [[18, 33], [45, 70]]
# print(matrix_search(data, 19))

# data = [[1, 2], [3, 4]]

# print(matrix_search(data, 1))
