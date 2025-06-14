def sort_numbers_from_one_to_three(nums: list[int]) -> None:
    dct = {1: 0, 2: 0, 3: 0}

    for elem in nums:
        dct[elem] += 1

    for i in range(dct.get(1)):
        nums[i] = 1
    for j in range(dct.get(1), dct.get(2) + dct.get(1)):
        nums[j] = 2
    for k in range(dct.get(1) + dct.get(2), dct.get(1) + dct.get(2) + dct.get(3)):
        nums[k] = 3


# nums = [2, 1, 3, 1, 3, 1, 3, 3]
# sort_numbers_from_one_to_three(nums)
# print(nums)
