def restore_values(nums: list[int]) -> list[int]:
    initial_min = min(nums) // 2
    return list(map(lambda x: x - initial_min, nums))


# assert restore_values([5, 9, 4, 7, 8]) == [3, 7, 2, 5, 6]
# assert restore_values([2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
# assert restore_values([1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]
# assert restore_values([-2, -4, 2, 5, -1, 0]) == [0, -2, 4, 7, 1, 2]
# assert restore_values([0, 0, 0, 0]) == [0, 0, 0, 0]
