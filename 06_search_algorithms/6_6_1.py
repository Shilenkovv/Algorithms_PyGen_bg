def binary_search(nums: list[int], target[int]):
    left, right = 0, len(nums) - 1
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
