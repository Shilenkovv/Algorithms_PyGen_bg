def section_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(1, n):
        if nums[i] == 0:
            continue

        item = nums[i]
        j = i - 1

        while j >= 0 and item < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = item


# nums = [2, 1, 0, 3, 2, 1, 0]
# section_sort(nums)
# print(nums)
