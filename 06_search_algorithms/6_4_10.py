def max_sum(nums: list[tuple[int, int]]) -> int:
    diffs_list = []
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += max(nums[i])
        diffs_list.append(abs(nums[i][1] - nums[i][0]))
    if cur_sum % 3:
        return cur_sum
    else:
        for diff in sorted(diffs_list):
            if (cur_sum - diff) % 3:
                return cur_sum - diff
    return -1


# assert max_sum([(1, 4), (2, 3), (2, 4), (5, 9)]) == 20
# assert max_sum([(1, 4), (2, 3), (2, 4), (5, 5)]) == 16
# assert max_sum([(2, 2), (2, 2), (2, 2), (2, 2)]) == 8
# assert max_sum([(1, 4), (5, 5), (1, 4), (5, 2)]) == -1
# assert max_sum([(2, 7)]) == 7
# assert max_sum([(5, 2), (2, 1), (4, 8)]) == 14
# assert max_sum([(2, 9)]) == 2
# assert max_sum([(3, 6)]) == -1
