def wave(nums: list) -> None:
    for i in range(1, len(nums), 2):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
