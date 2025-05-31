def sort_binary_list(nums: list[int]) -> None:
    ones_cnt = sum(nums)
    zeros_cnt = len(nums) - ones_cnt

    for i in range(len(nums)):
        if i + 1 <= zeros_cnt:
            nums[i] = 0
        else:
            nums[i] = 1


# binary_list = [0, 1, 1, 0, 1]
# sort_binary_list(binary_list)
# print(binary_list)
