def ranks_of_elements(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)
    sorted_dct = dict()

    rank = 1
    for elem in sorted_nums:
        if elem not in sorted_dct:
            sorted_dct[elem] = rank
            rank += 1

    for i in range(len(nums)):
        nums[i] = sorted_dct.get(nums[i])

    return nums


# print(ranks_of_elements([10, 20, 10, 30]))
