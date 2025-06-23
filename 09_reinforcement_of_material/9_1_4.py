def sort_by_value_and_index(nums: list[int]) -> None:
    indexed_values = [(val * (i + 1), val) for i, val in enumerate(nums)]
    indexed_values.sort()
    nums[:] = [val for _, val in indexed_values]


# nums = [11, 5, 2, 6, 3]
# sort_by_value_and_index(nums)
# print(nums)  # Результат: [2, 5, 11, 3, 6]
