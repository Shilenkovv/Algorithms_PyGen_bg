def sort_like_nums(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        idx_min = i
        elem_min = nums[idx_min] if isinstance(nums[idx_min], int) else nums[idx_min][0]

        for j in range(i + 1, n):
            elem = nums[j] if isinstance(nums[j], int) else nums[j][0]
            if elem < elem_min or (elem == elem_min and isinstance(nums[j], int)):
                idx_min = j
                elem_min = nums[idx_min] if isinstance(nums[idx_min], int) else nums[idx_min][0]
        if idx_min != i:
            nums[i], nums[idx_min] = nums[idx_min], nums[i]


# nums = [2, 1, [2], [3], 3]
# sort_like_nums(nums)
# print(nums) # [1, 2, [2], 3, [3]]
