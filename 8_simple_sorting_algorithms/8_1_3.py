def sort_by_digit_and_value(nums: list[int]) -> None:
    n = len(nums)

    for i in range(n - 1):
        idx_max = i

        for j in range(i + 1, n):
            if abs(nums[j]) % 10 > abs(nums[idx_max]) % 10:
                idx_max = j
            elif abs(nums[j]) % 10 == abs(nums[idx_max]) % 10 and nums[idx_max] > nums[j]:
                idx_max = j

        if idx_max != i:
            nums[i], nums[idx_max] = nums[idx_max], nums[i]


# nums = [5, 11, 183, 19, 274]
# sort_by_digit_and_value(nums)
# print(nums)  # [19, 5, 274, 183, 11]

# nums = [1]
# sort_by_digit_and_value(nums)
# print(nums)  # [1]

# nums = [11111, 1111, 111, 11, 1]
# sort_by_digit_and_value(nums)
# print(nums)  # [1, 11, 111, 1111, 11111]

# nums = [-2, 7, 6, -6, 2]
# sort_by_digit_and_value(nums)
# print(nums) # [7, -6, 6, -2, 2]
