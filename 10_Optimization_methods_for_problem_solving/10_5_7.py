def first_negative_in_every_sublist(nums: list[int], k: int) -> list[int]:
    left, neg_pointer = 0, 0

    ans = []
    negatives = [i for i in range(len(nums)) if nums[i] < 0]

    while left <= len(nums) - k:
        if len(negatives) != 0 and left <= negatives[neg_pointer] < left + k:
            ans.append(nums[negatives[neg_pointer]])
        else:
            ans.append(0)
        left += 1
        if len(negatives) != 0 and left - 1 == negatives[neg_pointer]:
            neg_pointer += 1

    return ans


# print(first_negative_in_every_sublist([2, -1, -3, 4, 1, 1, -4], 3))  # [-1, -1, -3, 0, -4]
# print(first_negative_in_every_sublist([2, 5, 6, 1, 0], 2))  # [0, 0, 0, 0]
