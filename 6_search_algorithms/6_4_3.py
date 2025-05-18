def max_difference(nums: list[int]) -> int:
    min_num = nums[0]
    max_diff = -1
    for i in range(1, len(nums)):
        if nums[i] > min_num:
            max_diff = max(max_diff, nums[i] - min_num)
        elif nums[i] < min_num:
            min_num = nums[i]
    return max_diff


assert max_difference([2, 5, 10, 2]) == 8
assert max_difference([8, 2, 6, 5]) == 4
assert max_difference([2, 6, 3, 11]) == 9
assert max_difference([7, 5, 4, 1]) == -1
assert max_difference([1, 2]) == 1
assert max_difference([1, 1]) == -1
assert max_difference([3, 1, 4]) == 3
assert max_difference([2, 9, 1, 3]) == 7
