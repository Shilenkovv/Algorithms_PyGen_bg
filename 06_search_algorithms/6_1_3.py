def search_insert_position(nums, target):
    if target == nums[0] or target < nums[0]:
        return 0
    for i in range(1, len(nums)):
        if nums[i] == target or target < nums[i]:
            return i
    return len(nums)
