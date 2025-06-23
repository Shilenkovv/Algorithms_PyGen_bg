def move_zeros(nums: list[int]) -> None:  # nums – список чисел
    n = len(nums)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] == 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break


nums = [1, 1, 1, 1]
move_zeros(nums)
print(nums)

nums = [0, 2, 1]
move_zeros(nums)
print(nums)
