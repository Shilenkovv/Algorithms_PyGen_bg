def two_sided_selection_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n // 2):
        idx_min = idx_max = i

        for j in range(i + 1, n - i):
            if nums[j] < nums[idx_min]:
                idx_min = j

            if nums[j] > nums[idx_max]:
                idx_max = j

        nums[i], nums[idx_min] = nums[idx_min], nums[i]

        if idx_max == i:
            idx_max = idx_min

        nums[n - i - 1], nums[idx_max] = nums[idx_max], nums[n - i - 1]


# nums = [3, 4, 1, 2, 5]
# two_sided_selection_sort(nums)
# print(nums)
