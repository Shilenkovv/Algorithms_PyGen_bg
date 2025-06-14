def move_zeros(nums: list[int]) -> None:
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0


# nums = [0, 1, 2]
# move_zeros(nums)
# print(nums)  # [1, 2, 0]

# nums = [0, 2, 0, 0, 1]
# move_zeros(nums)
# print(nums)  # [2, 1, 0, 0, 0]

# nums = [1, 2, 3]
# move_zeros(nums)
# print(nums)  # [1, 2, 3]

# nums = [1]
# move_zeros(nums)
# print(nums)  # [1]

# nums = [1, 1, 1, 1]
# move_zeros(nums)
# print(nums)  # [1, 1, 1, 1]

# nums = [0, 0, 0]
# move_zeros(nums)
# print(nums)  # [0, 0, 0]

# nums = [3, 2, 4, 0, 3, 2, 2, 5, 1, 4]
# move_zeros(nums)
# print(nums)
