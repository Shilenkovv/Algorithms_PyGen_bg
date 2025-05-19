def binary_search(data, target):
    ## list is reversed
    left, right = 0, len(data) - 1
    while left <= right:
        middle = left + (right - left) // 2
        elem = data[middle]
        if elem == target:
            return middle
        if elem < target:
            right = middle - 1
        else:
            left = middle + 1
    return -1
