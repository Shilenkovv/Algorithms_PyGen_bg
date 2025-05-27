def bubble_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        n_swaps = 0
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                n_swaps += 1
        if not swapped:
            break
    return n_swaps


# nums = [3, 4, 1, 2, 5]
# bubble_sort(nums)
# print(nums)
