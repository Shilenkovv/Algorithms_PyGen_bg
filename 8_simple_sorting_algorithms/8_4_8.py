def count_pairs_divisible_by_three(nums: list[int]) -> int:
    counts = [0, 0, 0]

    for num in nums:
        counts[num % 3] += 1

    ans = 0

    ans += counts[0] * (counts[0] - 1) // 2

    ans += counts[1] * counts[2]

    return ans
