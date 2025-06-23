def find_not_min_max(nums: list[int]) -> int:
    cur_min = min(nums)
    cur_max = max(nums)
    for num in nums:
        if num != cur_min and num != cur_max:
            return num
