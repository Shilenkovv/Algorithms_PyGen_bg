def ternary_search(nums: list[int], target):
    left, right = 0, len(nums) - 1
    block_size = (right - left) // 3
    left_middle, right_middle = left + block_size, right - block_size
    while left <= right:
        if nums[left_middle] == target:
            return True
        elif nums[right_middle] == target:
            return True
        if target < nums[left_middle]:
            right = left_middle - 1
        elif target > nums[right_middle]:
            left = right_middle + 1
        else:
            left = left_middle + 1
            right = right_middle - 1
        block_size = (right - left) // 3
        left_middle, right_middle = left + block_size, right - block_size
    return False


# assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8], 6)
# assert not ternary_search([1, 2, 3, 4, 5, 6, 7, 8], 10)
# assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8], 7)
