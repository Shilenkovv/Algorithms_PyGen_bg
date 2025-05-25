def sort_by_index(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        idx = i

        for j in range(i + 1, n):
            if i % 2:
                if nums[j] >= nums[idx] and j % 2:
                    idx = j
            else:
                if nums[j] <= nums[idx] and not j % 2:
                    idx = j
        if i != idx:
            nums[i], nums[idx] = nums[idx], nums[i]


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sort_by_index(nums)
# print(nums)  # [1, 10, 3, 8, 5, 6, 7, 4, 9, 2]

# nums = [6, 6, 2]
# sort_by_index(nums)
# print(nums)  # [2, 6, 6]
