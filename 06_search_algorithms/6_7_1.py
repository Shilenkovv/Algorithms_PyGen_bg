def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        middle = left + (right - left) // 2
        elem = data[middle]
        if elem == target:
            return middle
        if elem < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def matrix_search(matrix: list[list[int]], target):
    for row in matrix:
        ans = binary_search(row, target)
        if ans != -1:
            return True
    return False
