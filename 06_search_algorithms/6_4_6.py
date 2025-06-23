def max_divider(nums: list[int]) -> int:
    min_num = min(nums)
    for num in nums:
        if num % min_num:
            return -1
    return min_num
