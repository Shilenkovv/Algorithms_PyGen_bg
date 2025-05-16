def sequence_type(nums):
    is_constant = False
    is_increasing = False
    is_decreasing = False
    is_weakly_increasing = False
    is_weakly_decreasing = False

    if nums[0] == nums[1]:
        is_constant = True
        is_weakly_increasing = True
        is_weakly_decreasing = True
    elif nums[1] > nums[0]:
        is_increasing = True
        # is_weakly_increasing = True
    elif nums[1] < nums[0]:
        is_decreasing = True
        # is_weakly_decreasing = True
    for i in range(2, len(nums)):
        if nums[i] == nums[i - 1]:
            if is_decreasing:
                is_weakly_decreasing = True
            if is_increasing:
                is_weakly_increasing = True
            if is_increasing or is_decreasing:
                is_increasing = False
                is_decreasing = False
        elif nums[i] > nums[i - 1]:
            # is_increasing = True
            is_constant = False
            is_weakly_decreasing = False
            if is_decreasing:
                return 'RANDOM'
        elif nums[i] < nums[i - 1]:
            # is_decreasing = True
            is_constant = False
            is_weakly_increasing = False
            if is_increasing:
                return 'RANDOM'
    if is_constant:
        return 'CONSTANT'
    if is_weakly_increasing:
        return 'WEAKLY ASCENDING'
    if is_weakly_decreasing:
        return 'WEAKLY DESCENDING'
    if is_increasing:
        return 'ASCENDING'
    if is_decreasing:
        return 'DESCENDING'
