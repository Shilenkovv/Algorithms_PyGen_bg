def count_triplet_numbers(nums: list[int]) -> int:
    max_value = max(nums)
    counts = [0] * (max_value + 1)

    for elem in nums:
        counts[elem] += 1

    return len(list(filter(lambda x: x == 3, counts)))
