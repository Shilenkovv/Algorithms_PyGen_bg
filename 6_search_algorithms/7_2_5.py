def find_max_ratio(nums: list[int]) -> float:
    cur_min = float('inf')
    cur_max = -float('inf')
    cur_min_ind = cur_max_ind = 0
    max_ratio = -1
    for i in range(len(nums)):
        if nums[i] < cur_min:
            cur_min = nums[i]
            cur_min_ind = i
            cur_max = -float('inf')
            cur_max_ind = -1
        elif nums[i] > cur_max:
            cur_max, cur_max_ind = nums[i], i
        if i in [cur_max_ind, cur_min_ind] and cur_max_ind > cur_min_ind and cur_max != cur_min:
            max_ratio = max(max_ratio, cur_max / cur_min)
    return max_ratio


# print(find_max_ratio([3, 2, 4, 8, 1]))
# print(find_max_ratio([5, 4, 3, 2, 1]))
# print(find_max_ratio([1, 2, 10, 4]))
