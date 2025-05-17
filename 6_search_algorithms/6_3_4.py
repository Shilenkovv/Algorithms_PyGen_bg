def min_max_diff(nums: list[int]) -> int:
    cur_max = -float('inf')
    cur_min = float('inf')
    for num in nums:
        if num > cur_max:
            cur_max = num
        if num < cur_min:
            cur_min = num
    return cur_max - cur_min
