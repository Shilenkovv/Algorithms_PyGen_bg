def is_majority_element(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    n = len(nums)
    return left + n // 2 < n and nums[left + n // 2] == target
