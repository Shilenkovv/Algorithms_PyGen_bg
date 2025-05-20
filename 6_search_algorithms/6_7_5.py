def lower_bound(nums: list[int], target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        elem = nums[middle]
        if elem == target:
            while middle > 0 and nums[middle - 1] == target:
                middle -= 1
            return middle
        if elem < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


# assert lower_bound([10, 11, 12, 13, 14, 15], 14) == 4
# assert lower_bound([10, 11, 12, 13, 14, 15], 20) == -1
# assert lower_bound([10, 11, 12, 12, 12, 13], 12) == 2
# assert lower_bound([1, 1, 1, 1, 1], 1) == 0
