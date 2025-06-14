def sort_half_sorted(nums: list[int]) -> list[int]:
    n = len(nums)
    mid = (n + 1) // 2

    result = []
    i = 0
    j = mid

    while i < mid and j < n:
        if nums[i] < nums[j]:
            result.append(nums[i])
            i += 1
        else:
            result.append(nums[j])
            j += 1

    while i < mid:
        result.append(nums[i])
        i += 1

    while j < n:
        result.append(nums[j])
        j += 1

    return result
