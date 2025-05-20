def equal(nums: list[int]):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == middle:
            while middle > 0 and nums[middle - 1] == middle - 1:
                middle -= 1
            return middle
        if nums[middle] < middle:
            left = middle + 1
        else:
            right = middle - 1
    return -1
