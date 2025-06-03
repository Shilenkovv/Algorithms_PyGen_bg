def valid_nums_in_segments(nums: list[int], segments: list[tuple[int, int]]) -> list[int]:
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums) - 1):
        prefix_sum[i + 1] = prefix_sum[i] + int(nums[i + 1] > nums[i])

    ans = []
    for s, e in segments:
        ans.append(prefix_sum[e] - prefix_sum[s])
    return ans


# print(valid_nums_in_segments([4, 8, 9, 5, 4, 3, 2, 5], [(0, 3), (2, 5), (5, 7)]))  # [2, 0, 1]
