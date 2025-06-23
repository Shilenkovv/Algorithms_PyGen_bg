def first_even(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] % 2:
            left = mid + 1
        # elif mid != 0 and nums[mid - 1] % 2:
        else:
            right = mid - 1
    return left


# print(first_even([1, 3, 4, 6, 8]))  # 2
# print(first_even([1, 3, 5, 7, 2]))  # 4
# print(first_even([1, 2]))  # 1
