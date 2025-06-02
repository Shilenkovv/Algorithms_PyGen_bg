def can_be_sorted(nums, increasing=True):
    removed = 0
    previous_value = float('-inf') if increasing else float('inf')
    current_value = previous_value

    for num in nums:
        if increasing:
            if num > current_value:
                previous_value = current_value
                current_value = num
            elif num > previous_value:
                removed += 1
                current_value = num
            else:
                removed += 1

        else:
            if num < current_value:
                previous_value = current_value
                current_value = num
            elif num < previous_value:
                removed += 1
                current_value = num
            else:
                removed += 1

        if removed > 1:
            return False

    return True


def is_almost_sorted(sequence):
    return can_be_sorted(sequence, increasing=True) or can_be_sorted(sequence, increasing=False)
