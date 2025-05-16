def linear_search(nums, target, reverse=False):
    rng = range(len(nums) - 1, -1, -1) if reverse else range(len(nums))
    for i in rng:
        if nums[i] == target:
            return i
    return -1
