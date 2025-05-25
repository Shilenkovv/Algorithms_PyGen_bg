def sort_only_odds(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        if not nums[i] % 2:
            continue
        idx_min = i

        for j in range(i + 1, n):
            if nums[j] <= nums[idx_min] and nums[j] % 2:
                idx_min = j

        if i != idx_min:
            nums[i], nums[idx_min] = nums[idx_min], nums[i]


# nums = [5, 8, 6, 3, 4, 1]
# sort_only_odds(nums)
# print(nums)  # [1, 8, 6, 3, 4, 5]
