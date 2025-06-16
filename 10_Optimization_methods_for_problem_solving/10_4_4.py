def count_pairs_with_greater_difference(nums: list[int], k: int) -> int:
    i, j = 0, min(len(nums) - 1, 1)
    counter = 0

    while i < len(nums) - 1 and j < len(nums):
        if nums[j] - nums[i] > k:
            counter += len(nums) - j
            i += 1
        else:
            j += 1
    return counter


# nums = [1, 2, 4, 8, 10]
# print(
#     count_pairs_with_greater_difference(nums, 4)
# )  # пары: (1, 10), (2, 10), (4, 10), (1, 8), (2, 8) # 5
# nums = [3, 4, 5, 8, 10]
# print(count_pairs_with_greater_difference(nums, 10))  # подходящих пар нет # 0
# nums = [5]
# print(count_pairs_with_greater_difference(nums, 1))  # подходящих пар нет # 0
# nums = [1, 1, 1, 1, 1]
# print(count_pairs_with_greater_difference(nums, 1))  # подходящих пар нет # 0
# nums = [1, 2, 3]
# print(count_pairs_with_greater_difference(nums, 1))  # (3, 1) # 1
