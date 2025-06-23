def max_common_sum(nums: list[int]) -> int:
    counts = [0] * 19

    for elem in nums:
        two_dig = elem % 100
        counts[two_dig % 10 + two_dig // 10] += 1

    max_sum = -float('inf')
    max_cnt = -float('inf')
    for i in range(len(counts)):
        if counts[i] and counts[i] >= max_cnt:
            max_cnt = counts[i]
            max_sum = i
    return max_sum


# print(max_common_sum([121, 21, 2221, 1122, 3322, 22]))
