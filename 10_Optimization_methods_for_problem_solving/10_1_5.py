def zeros_in_segments(nums: list[int], segments: list[tuple[int, int]]) -> list[int]:
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + int(nums[i] == 0)

    ans = []
    for s, e in segments:
        ans.append(prefix_sum[e + 1] - prefix_sum[s])
    return ans


# print(zeros_in_segments([2, 0, 6, 1, 0, 4, 2, 0], [(0, 7), (2, 3), (4, 7)]))
