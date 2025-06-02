def bound_sort(nums: list[int], k: int) -> bool:
    if k == len(nums) - 1:
        return True
    max_elem = max(nums[: k + 1])
    if nums[k + 1] < max_elem:
        return False
    for i in range(k + 2, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


# print(bound_sort([2, 7, 4, 1, 8, 9], 3))  # True
# print(bound_sort([7, 2, 1, 4, 5, 6], 2))  # False
# print(bound_sort([9, 7, 6, 1, 3, 4], 5))  # True
# print(bound_sort([2, 7, 4, 1, 80, 9], 3))  # False
# print(bound_sort([1], 0))  # True
