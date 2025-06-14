def largest_possible_number(nums: list[int]) -> int:
    n = len(nums)

    for i in range(n):
        nums[i] = str(nums[i])

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return int(''.join(nums))
