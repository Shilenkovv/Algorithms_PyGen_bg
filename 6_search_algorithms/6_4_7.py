def max_ascending_sum(nums: list[int]) -> int:
    cur_sum = nums[0]
    max_sum = -float('inf')
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur_sum += nums[i]
        else:
            max_sum = max(max_sum, cur_sum)
            cur_sum = nums[i]
    return max(max_sum, cur_sum)


# assert max_ascending_sum([91, 5, 65, 49, 86]) == 135
