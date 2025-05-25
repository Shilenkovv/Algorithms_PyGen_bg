def alter_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        idx = i

        for j in range(i + 1, n):
            if not i % 2:
                if nums[j] > nums[idx]:
                    idx = j
            else:
                if nums[j] < nums[idx]:
                    idx = j
        if i != idx:
            nums[i], nums[idx] = nums[idx], nums[i]


# nums = [1, 2, 3, 4, 5]
# alter_sort(nums)
# print(nums)  # [5, 1, 4, 2, 3]
