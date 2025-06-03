def has_sublist_with_sum(nums: list[int], k: int) -> bool:
    seen_sums = set()
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum == k:
            return True
        if (current_sum - k) in seen_sums:
            return True
        seen_sums.add(current_sum)

    return False


# print(has_sublist_with_sum([3, -2, 5, 1, 2], 4))  # [-2, 5, 1] True
# print(has_sublist_with_sum([-3, -2, -5, -2, 0], -9)) # [-2, -5, -2] True
# print(has_sublist_with_sum([1, 2, 3, 4, 5], 9))  # True [4, 5]
