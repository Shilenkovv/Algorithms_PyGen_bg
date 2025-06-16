from collections import Counter


def has_triplet_with_zero_sum(nums: list[int]) -> bool:
    seen = Counter(nums)

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if -(nums[i] + nums[j]) in seen:
                if not (nums[i] == nums[j] == 0 and seen.get(0) <= 2):
                    return True
    return False


# print(has_triplet_with_zero_sum([1, 2, -3, 4, -2]))  # True
# print(has_triplet_with_zero_sum([1, 2, 3, 4, 5]))  # False
# print(has_triplet_with_zero_sum([0, 0, 0, 0, 0]))  # True
# print(has_triplet_with_zero_sum([0, 0, 1]))  # False
