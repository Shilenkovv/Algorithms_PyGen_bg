def priority_sort(nums: list[int], priority_nums: set[int]) -> None:
    nums.sort(key=lambda x: (x not in priority_nums, x))


nums = [4, 3, 1, 5, 2]
priority_nums = {3, 4}
priority_sort(nums, priority_nums)
print(nums)
