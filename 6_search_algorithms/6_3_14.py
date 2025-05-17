def max_consecutive_ones(nums: list[int]) -> int:
    max_streak = cur_streak = 0
    for num in nums:
        if num == 1:
            cur_streak += 1
        else:
            max_streak = max(max_streak, cur_streak)
            cur_streak = 0
    return max(max_streak, cur_streak)
