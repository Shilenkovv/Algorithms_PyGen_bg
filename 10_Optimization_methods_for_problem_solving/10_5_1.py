def max_average_sublist(nums: list[int], k: int) -> float:
    left, right = 0, k - 1
    window_sum = 0

    for i in range(k):
        window_sum += nums[i]

    window_avg_max = window_sum / k

    while right < len(nums) - 1:
        left += 1
        right += 1
        window_sum = window_sum - nums[left - 1] + nums[right]
        window_avg = window_sum / k
        window_avg_max = max(window_avg_max, window_avg)

    return window_avg_max


# print(max_average_sublist([2, 1, 5, 3, 1, 4], 3))  # (1 + 5 + 3) / 3 = 3 # 3.0
# print(max_average_sublist([4, -1, 3, -2, 7, 5], 4))  # (3 - 2 + 7 + 5) / 4 = 3.25 # 3.25
# print(max_average_sublist([5], 1))  # 5 / 1 = 5.0 # 5.0
# print(max_average_sublist([1, 2, 3, 4, 5, 6], 1))  # 6 / 1 = 6.0 # 6.0
# print(max_average_sublist([-1, 0, 1], 3))  # (-1 + 0 + 1) / 3 = 0.0 # 0.0
# print(max_average_sublist([-3, -5, -2, -3, -4], 2))  # (-5 - 2) / 2 = -2.5 # -2.5
