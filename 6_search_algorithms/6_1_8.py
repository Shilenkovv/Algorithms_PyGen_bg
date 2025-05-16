def count_occurrences(nums, target, start, end):
    ans = 0
    if start == end or start >= len(nums):
        return ans
    for i in range(len(nums)):
        if i < start:
            continue
        elif i >= start and i <= end - 1 and nums[i] == target:
            ans += 1
        elif i >= end:
            break
    return ans
