def odd_even_sort(nums: list[int]) -> None:
    odd_nums = sorted([x for x in nums if x % 2])
    even_nums = sorted([x for x in nums if not x % 2], reverse=True)
    for i in range(len(odd_nums)):
        nums[i] = odd_nums[i]
    for j in range(len(even_nums)):
        nums[j + len(odd_nums)] = even_nums[j]


# nums = [5, 4, 9, 1, 6, 3]
# odd_even_sort(nums)
# print(nums)  # [1, 3, 5, 9, 6, 4]
