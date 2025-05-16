def find_sum_indexes(nums, value):
    start = 0
    end = 0
    cur_sum = nums[0]
    while end < len(nums):
        if cur_sum == value:
            # if end - start - 1 == len(nums):
            #     return -1
            return start, end
        elif cur_sum < value:
            if end == len(nums) - 1:
                return -1
            end += 1
            cur_sum += nums[end]
        elif cur_sum > value:
            cur_sum -= nums[start]
            start += 1
    return -1
