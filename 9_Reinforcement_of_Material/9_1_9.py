def sort_only_positives(nums: list[int]) -> None:
    positives = sorted([num for num in nums if num > 0])
    cur_ind = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[i] = positives[cur_ind]
            cur_ind += 1
        if cur_ind == len(positives):
            break


# nums = [5, 2, -3, 5, -7, 3, -3, -20, -10, -15]
# sort_only_positives(nums)
# print(nums)
