def elements_in_the_range(nums, start, end):
    if end == 0:
        return False
    if start == end:
        tot_sum = start
        tot_cnt = 1
    else:
        tot_cnt = end - start + 1
        tot_sum = ((start + end) * tot_cnt) // 2
    seen_set = set()
    cur_cnt = 0
    cur_sum = 0
    for i in range(len(nums)):
        if nums[i] >= start and nums[i] <= end and nums[i] not in seen_set:
            cur_sum += nums[i]
            cur_cnt += 1
            seen_set.add(nums[i])
    return cur_cnt == tot_cnt and cur_sum == tot_sum
