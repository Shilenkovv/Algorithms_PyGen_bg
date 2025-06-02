def find_triple(nums: list[int]) -> list[int]:
    nums.sort()
    max_val = nums[-1] - nums[0]
    return [nums[1] - max_val, nums[2] - max_val, max_val]


# print(find_triple([8, 5, 7, 4]))
