def count_beautiful_pairs(nums: list[int]) -> int:
    max_value = max(nums)
    counts = [0] * (max_value + 1)

    for elem in nums:
        counts[elem] += 1

    return sum(list(map(lambda x: x // 2, counts)))


# print(least_frequent_number([4, 2, 4, 1, 3, 2, 1]))
