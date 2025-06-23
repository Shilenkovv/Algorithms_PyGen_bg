def largest_gap(nums: list[int]) -> int:
    nums.sort()

    max_diff = -float('inf')
    for i in range(1, len(nums)):
        max_diff = max(max_diff, abs(nums[i] - nums[i - 1]))
    return max_diff
