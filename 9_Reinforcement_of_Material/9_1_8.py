def min_steps_to_sort(nums: list[int]) -> int:
    tot_steps = 0
    tmp_elem = nums[0]
    for i in range(1, len(nums)):
        tmp_elem = max(tmp_elem + 1, nums[i])
        tot_steps += max(0, tmp_elem - nums[i])

    return tot_steps


# print(min_steps_to_sort([-4, -5, 4, -2, 7, -8, 4, -4, -3, -2]))
