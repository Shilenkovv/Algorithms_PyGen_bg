def pair_with_sum(nums: list[int], k: int) -> tuple[int, int]:
    nums_set = set(nums)
    for elem in nums:
        if elem != k - elem and k - elem in nums_set:
            return (min(elem, k - elem), max(elem, k - elem))


# print(pair_with_sum([1, 16, 9, 10, 4], 26)) # (10, 16)
