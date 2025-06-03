def difference_list(nums: list[int]) -> list[int]:
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    ans = []
    for i in range(1, len(prefix_sum)):
        ans.append(abs(prefix_sum[i - 1] - (prefix_sum[-1] - prefix_sum[i])))
    return ans


# print(difference_list([2, 3, 6, 1, 4]))  # [14, 9, 0, 7, 12]
