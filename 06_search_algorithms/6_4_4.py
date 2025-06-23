def get_closest_element(nums: list[int], target: int) -> int:
    if len(nums) == 1:
        return nums[0]
    min_diff = float('inf')
    potential_num = -float('inf')
    for num in nums:
        curr_diff = abs(num - target)
        if curr_diff <= min_diff:
            potential_num = max(potential_num, num) if curr_diff == min_diff else num
            min_diff = curr_diff
    return potential_num


# assert get_closest_element([5, 4, 3, 2, 1], 3) == 3
# assert get_closest_element([1, -1, 3], 0) == 1
# assert get_closest_element([-1, 1, 3], 0) == 1
# assert get_closest_element([0], 100) == 0
