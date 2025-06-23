def min_steps_to_make_equal(nums: list[int]) -> int:
    new_nums = sorted(nums)
    elem = new_nums[len(new_nums) // 2]
    return sum(map(lambda x: abs(elem - x), new_nums))


# print(min_steps_to_make_equal([2, 3, 1, 5, 2]))
