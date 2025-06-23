def missing_number(n: int, nums: list[int]) -> int:
    return ((1 + n) * n) // 2 - sum(nums)
