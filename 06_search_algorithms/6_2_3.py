def kth_occurrence(nums, target, k):
    if k > len(nums):
        return -1
    seen_times = 0
    for i in range(len(nums)):
        if nums[i] == target:
            seen_times += 1
            if seen_times == k:
                return i
    return -1
