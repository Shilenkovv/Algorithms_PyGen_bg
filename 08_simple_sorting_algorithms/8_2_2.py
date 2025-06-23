def number_of_swaps(nums: list[int]) -> int:  # nums – список чисел
    n = len(nums)
    n_swaps = 0

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                n_swaps += 1
        if not swapped:
            break
    return n_swaps
