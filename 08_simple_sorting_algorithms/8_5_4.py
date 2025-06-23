def sort_by_length_and_value(nums: list[int]) -> None:
    nums.sort(key=lambda x: (-len(str(abs(x))), x))


# nums = [8, 13, 183, 9, 26, 229]
# sort_by_length_and_value(nums)
# print(nums)
