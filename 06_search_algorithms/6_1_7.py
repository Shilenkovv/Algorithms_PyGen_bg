def doubling_the_value(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            value *= 2
            nums[i] = value
    return value
