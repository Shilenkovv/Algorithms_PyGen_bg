def max_sum(nums: list[int]) -> int:
    cur_max_sum = -1
    cur_sum = 0
    found_negative = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            found_negative += 1
            cur_max_sum = max(cur_max_sum, cur_sum) if found_negative > 1 else -1
            cur_sum = 0
        elif found_negative != 0:
            cur_sum += nums[i]
    return cur_max_sum if found_negative > 1 else -1


assert max_sum([1, -2, -3, 4]) == 0
assert max_sum([1, -2, 3, 4, -5]) == 7
assert max_sum([-1, 2, 3, -5, 6, 7, -8]) == 13
assert max_sum([1, 2, -3, 4, 5]) == -1
assert max_sum([1, 2, 3, 4, 5]) == -1
assert max_sum([-1, -2]) == 0
