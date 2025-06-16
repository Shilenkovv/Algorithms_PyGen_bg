def pair_with_lower_or_equal_difference(nums: list[int], k: int) -> int:
    i, j = 0, min(len(nums) - 1, 1)

    max_diff = -float('inf')
    ans = None

    while i < len(nums) - 1 and j < len(nums):
        if i == j:
            j += 1
            continue
        curr_diff = nums[j] - nums[i]
        if curr_diff <= k and curr_diff > max_diff:
            max_diff = curr_diff
            ans = (nums[i], nums[j])
            j += 1
        elif curr_diff > k:
            i += 1
        else:
            j += 1

    return ans


# print(pair_with_lower_or_equal_difference([2, 4, 7, 8, 10, 11], 3))  # (4, 7)
# print(pair_with_lower_or_equal_difference([2, 3, 4, 7, 8, 10, 11], 2))  # (2, 4)
# print(pair_with_lower_or_equal_difference([1, 2, 3, 4], 0))  # None
