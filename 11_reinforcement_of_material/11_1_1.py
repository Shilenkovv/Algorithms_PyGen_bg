def swap_tail_head(nums: list[int]) -> None:
    n = len(nums)
    for i in range(n // 2):
        nums[i], nums[i + n // 2 + n % 2] = nums[i + n // 2 + n % 2], nums[i]


# nums = [1, 2, 3, 4, 5]
# swap_tail_head(nums)
# print(nums)
