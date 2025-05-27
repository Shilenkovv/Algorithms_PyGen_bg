def cocktail_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        swapped = False
        for j in range(i, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        for k in range(n - i - 1, i, -1):
            if nums[k] < nums[k - 1]:
                nums[k], nums[k - 1] = nums[k - 1], nums[k]
                swapped = True
        if not swapped:
            break


data = [8, 9, 6, 5, 7, 4, 1, 2, 3]
cocktail_sort(data)
print(data)
