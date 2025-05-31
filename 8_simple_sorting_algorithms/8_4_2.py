def least_frequent_number(nums: list[int]) -> int:
    max_value = max(nums)
    counts = [0] * (max_value + 1)

    for elem in nums:
        counts[elem] += 1

    ans_cnt = float('inf')
    ans = -1

    for i in range(len(counts)):
        if counts[i] and counts[i] < ans_cnt:
            ans_cnt = counts[i]
            ans = i

    return ans


# print(least_frequent_number([4, 2, 4, 1, 3, 2, 1]))
