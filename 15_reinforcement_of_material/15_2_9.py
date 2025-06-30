def extra_num(n: int, nums: list[int]) -> int:
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return actual_sum - expected_sum
