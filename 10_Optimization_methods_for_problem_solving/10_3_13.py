def duplicate_zeros(nums: list[int]) -> None:
    dupl = nums[:]

    dupl_idx = 0
    main_idx = 0

    while main_idx < len(nums):
        if dupl[dupl_idx] != 0:
            nums[main_idx] = dupl[dupl_idx]
            main_idx += 1
            dupl_idx += 1
        elif dupl[dupl_idx] == 0:
            nums[main_idx] = 0
            main_idx += 1
            if main_idx < len(nums):
                nums[main_idx] = 0
                main_idx += 1
                dupl_idx += 1


# nums = [3, 0, 2, 7, 0, 1, 4, 5]  # [3, 0, 0, 2, 7, 0, 0, 1]
# duplicate_zeros(nums)
# print(nums)
