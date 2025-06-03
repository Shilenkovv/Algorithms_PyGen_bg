def difference_list(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    result = [0] * n
    for i in range(n):
        left_sum = nums[i] * i - (prefix_sum[i - 1] if i > 0 else 0)
        right_sum = (prefix_sum[n - 1] - prefix_sum[i]) - nums[i] * (n - i - 1)
        result[i] = left_sum + right_sum

    return result


# print(difference_list([1, 4, 6]))  # [8, 5, 7]
