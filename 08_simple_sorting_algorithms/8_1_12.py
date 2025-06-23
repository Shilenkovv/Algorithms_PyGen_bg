def double_selection_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(0, n - 1, 2):
        index_min1, index_min2 = i, i + 1

        for j in range(i + 1, n):
            if nums[j] < nums[index_min1]:
                index_min2 = index_min1
                index_min1 = j
            elif nums[j] < nums[index_min2]:
                index_min2 = j

        nums[i], nums[index_min1] = nums[index_min1], nums[i]

        if index_min2 == i:
            index_min2 = index_min1

        nums[i + 1], nums[index_min2] = nums[index_min2], nums[i + 1]


# data = [0, 6, -5, 6, 7]
# selection_sort(data)
# print(data)


# nums = [-7, -6, -2, -10]
# double_selection_sort(nums)
# print(nums)
