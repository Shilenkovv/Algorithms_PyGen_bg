def has_duplicates_within_range(nums: list[int], k: int) -> bool:
    left = 0
    right = min(len(nums), k)

    seen = set()
    for i in range(right):
        seen.add(nums[i])

    while right < len(nums):
        if len(seen) < k:
            return True
        left += 1
        right += 1
        seen.add(nums[right - 1])
        seen.remove(nums[left - 1])

    return False if len(seen) == k else True


# print(has_duplicates_within_range([3, 1, 5, -4, 5, 2], 3))  # True
# print(has_duplicates_within_range([1, 1, 5, -4, 2, 5], 3))  # True
# print(has_duplicates_within_range([5, 1, 3, -4, 2, 5], 3))  # False
# print(has_duplicates_within_range([5, 1, 3, -4, 2, 5], 6))  # True
# print(has_duplicates_within_range([5, 1, 3, -4, 2, 2], 2))  # True
