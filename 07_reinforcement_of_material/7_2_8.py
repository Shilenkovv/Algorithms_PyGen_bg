def count_ones(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == 0:
            left = mid + 1
        elif nums[mid] == 1:
            if mid != 0 and nums[mid - 1] == 0:
                return len(nums) - mid
            else:
                right = mid - 1
    return len(nums) - left


# print(count_ones([1, 1, 1, 1, 1]))
# print(count_ones([0, 0, 0, 1, 1]))
# print(count_ones([0, 0, 0, 0, 0]))
# print(count_ones([1]))
# print(count_ones([0, 1]))
