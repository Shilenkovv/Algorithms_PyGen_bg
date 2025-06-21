def shortest_sublist_with_greater_sum(nums: list[int], k: int) -> list[int]:
    left = window_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > k:
            window_sum -= nums[left]
            min_length = min(min_length, right - left + 1)
            left += 1

    return -1 if min_length == float('inf') else min_length


# print(
#     shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 9)
# )  # [3, 4, 2, 1], 3 + 4 + 2 + 1 = 10 # 4
# print(
#     shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 11)
# )  # [4, 2, 1, 5], 4 + 2 + 1 + 5 = 12 # 4
# print(
#     shortest_sublist_with_greater_sum([1, 3, 4, 2, 1, 5, 1], 20)
# )  # подходящих подсписков нет # -1
# print(shortest_sublist_with_greater_sum([5], 1))
