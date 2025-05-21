def find_index(nums, target) -> int:
    left = 0
    right = 1

    while nums[right] < target:
        right *= 2
    left = right // 2

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
