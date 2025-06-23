def max_to_min(nums: list[int]) -> None:
    cur_max = max(nums)
    cur_min = min(nums)
    for i in range(len(nums)):
        if nums[i] == cur_max:
            nums[i] = cur_min
    return
