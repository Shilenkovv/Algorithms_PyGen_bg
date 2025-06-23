def max_sum(nums: list[int]) -> int:
    if max(nums) <= 0:
        return max(nums)
    cur_sum = 0
    for num in nums:
        if num > 0:
            cur_sum += num
    return cur_sum
