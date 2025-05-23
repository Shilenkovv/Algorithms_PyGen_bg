def count_maxes(nums: list[int]) -> int:
    max_elem = max(nums)
    max_cnt = 0
    for elem in nums:
        if elem == max_elem:
            max_cnt += 1
    return max_cnt
