def binary_search(nums, target):
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        return -1
    if nums[1] > nums[0]:
        is_ascending = True
    else:
        is_ascending = False
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        elem = nums[middle]
        if elem == target:
            return middle
        if elem < target:
            if is_ascending:
                left = middle + 1
            else:
                right = middle - 1
        else:
            if is_ascending:
                right = middle - 1
            else:
                left = middle + 1
    return -1
