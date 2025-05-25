def selection_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        index_max = i

        for j in range(i + 1, n):
            if nums[j] > nums[index_max]:
                index_max = j

        if i != index_max:
            nums[i], nums[index_max] = nums[index_max], nums[i]


# data = [0, 6, -5, 6, 7]
# selection_sort(data)
# print(data)
