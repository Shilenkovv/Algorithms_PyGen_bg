def min_valid_index(nums: list[int], k: int, m: int) -> list[int]:
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    for i in range(len(prefix_sum) - k - 1):
        if prefix_sum[i + k + 1] - prefix_sum[i] == m:
            return i
    return -1


# print(min_valid_index([7, 2, 3, 1, 4, 1, 1], 2, 6))  # [2, 3, 1]
