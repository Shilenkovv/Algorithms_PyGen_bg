def min_difference_pairs(nums: list[int]) -> list[tuple[int, int]]:
    new_nums = sorted(nums)
    min_diff = float('inf')

    for i in range(1, len(new_nums)):
        min_diff = min(min_diff, new_nums[i] - new_nums[i - 1])

    result = []
    for i in range(1, len(new_nums)):
        if new_nums[i] - new_nums[i - 1] == min_diff:
            result.append((new_nums[i - 1], new_nums[i]))
    return result


# print(min_difference_pairs([2, 3, 4, 5, 1]))  # [(1, 2), (2, 3), (3, 4), (4, 5)]
# print(min_difference_pairs([1, 3, 8, 6, 11]))  # [(1, 3), (6, 8)]
