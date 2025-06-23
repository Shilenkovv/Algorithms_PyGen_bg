def count_beautiful_pairs(nums: list[int]) -> int:
    counts = [False] * 1001
    for elem in nums:
        counts[elem] = True

    bp = 0
    for i in range(1000, 0, -1):
        if counts[i]:
            bp += sum(counts[:i])
    return bp


# print(count_beautiful_pairs([1, 4, 3, 2]))
# print(count_beautiful_pairs([1, 2]))
# print(count_beautiful_pairs([1]))
# print(count_beautiful_pairs([1, 1, 1, 1, 1]))
