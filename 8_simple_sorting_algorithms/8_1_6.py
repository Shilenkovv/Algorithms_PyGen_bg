def sort_except_one(nums: list[int], k: int) -> None:
    n = len(nums)

    for i in range(n - 1):
        if i == k:
            continue
        idx_min = i

        for j in range(i + 1, n):
            if nums[j] <= nums[idx_min] and j != k:
                idx_min = j

        if i != idx_min:
            nums[i], nums[idx_min] = nums[idx_min], nums[i]


# nums = [2, 4, 6, 1, 3, 5]
# sort_except_one(nums, 2)
# print(nums)  # [1, 2, 6, 3, 4, 5]
