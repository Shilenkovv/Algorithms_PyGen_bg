def count_mismatches(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    mismatches = 0

    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            mismatches += 1
    return mismatches
