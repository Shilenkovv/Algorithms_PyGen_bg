from collections import defaultdict


def uniques_count_in_every_sublist(nums: list[int], k: int) -> list[int]:
    left = 0
    right = k

    seen = defaultdict(int)
    for i in range(k):
        seen[nums[i]] += 1
    ans = [len(seen)]
    while right < len(nums):
        left += 1
        right += 1
        seen[nums[left - 1]] -= 1
        seen[nums[right - 1]] += 1
        if seen[nums[left - 1]] == 0:
            seen.pop(nums[left - 1])
        ans.append(len(seen))

    return ans


# print(uniques_count_in_every_sublist([2, 5, 5, 5, -3, 1, -3], 3))  # [2, 1, 2, 3, 2]
# print(has_duplicates_within_range([3, 1, 5, -4, 5, 2], 3))  # True
# print(has_duplicates_within_range([1, 1, 5, -4, 2, 5], 3))  # True
# print(has_duplicates_within_range([5, 1, 3, -4, 2, 5], 3))  # False
# print(has_duplicates_within_range([5, 1, 3, -4, 2, 5], 6))  # True
# print(has_duplicates_within_range([5, 1, 3, -4, 2, 2], 2))  # True
