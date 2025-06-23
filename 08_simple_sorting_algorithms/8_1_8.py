def sort_by_parity(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        idx = i

        for j in range(i + 1, n):
            if nums[i] % 2:
                if nums[j] <= nums[idx] and nums[j] % 2:
                    idx = j
            else:
                if nums[j] >= nums[idx] and not nums[j] % 2:
                    idx = j
        if i != idx:
            nums[i], nums[idx] = nums[idx], nums[i]


# nums = [6, 8, 2, 4, 0]  # все элементы четные
# sort_by_parity(nums)
# print(nums)
