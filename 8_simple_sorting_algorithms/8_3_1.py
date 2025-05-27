def insertion_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(1, n):
        item = nums[i]

        j = i - 1
        while j >= 0 and item > nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item


# nums = [3, 4, 1, 2, 5]
# insertion_sort(nums)
# print(nums)
