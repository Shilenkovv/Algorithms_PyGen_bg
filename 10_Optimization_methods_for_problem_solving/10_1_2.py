def restore_by_prefix_sum(p: list[int]) -> list[int]:
    nums = [0] * (len(p) - 1)
    for i in range(1, len(p)):
        nums[i - 1] = p[i] - p[i - 1]
    return nums


# print(restore_by_prefix_sum([0, 10, 14, 20, 21, 29]))
