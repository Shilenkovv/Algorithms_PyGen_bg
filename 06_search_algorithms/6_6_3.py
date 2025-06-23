def bounded_binary_search(nums, target, left=0, right=float('inf')):
    if right == float('inf'):
        right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        elem = nums[middle]
        if elem == target:
            return middle
        if elem < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
