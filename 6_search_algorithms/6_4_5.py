def steps_to_max(nums: list[int]) -> int:
    max_elem = max(nums)
    steps = 0
    for num in nums:
        steps += max_elem - num
    return steps


# assert get_closest_element([5, 4, 3, 2, 1], 3) == 3
# assert get_closest_element([1, -1, 3], 0) == 1
# assert get_closest_element([-1, 1, 3], 0) == 1
# assert get_closest_element([0], 100) == 0
