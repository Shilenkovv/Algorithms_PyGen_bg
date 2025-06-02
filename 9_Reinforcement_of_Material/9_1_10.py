def is_permutation(nums: list[int]) -> bool:
    return sum(nums) == ((1 + len(nums)) * len(nums)) // 2 and len(nums) == len(set(nums))


# print(is_permutation([2, 3, 1, 4]))
# print(is_permutation([3, 1, 4]))
# print(is_permutation([2, 3, 4, 6, 5]))
# print(is_permutation([2, 3, 4, 6, 5, 1]))
