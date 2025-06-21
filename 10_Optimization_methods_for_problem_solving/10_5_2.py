def negatives_count_in_every_sublist(nums: list[int], k: int) -> list[int]:
    left, right = 0, k - 1
    curr_negatives = 0
    negatives_cnt = []

    for i in range(k):
        if nums[i] < 0:
            curr_negatives += 1
    negatives_cnt.append(curr_negatives)

    while right < len(nums) - 1:
        left += 1
        right += 1
        if nums[right] < 0:
            curr_negatives += 1
        if nums[left - 1] < 0:
            curr_negatives -= 1
        negatives_cnt.append(curr_negatives)

    return negatives_cnt


# print(negatives_count_in_every_sublist([2, -1, -3, 4, 1, 1, -4], 3))  # [2, 2, 1, 0, 1]
