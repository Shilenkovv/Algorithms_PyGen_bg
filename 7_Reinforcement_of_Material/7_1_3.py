def min_distance_between_peaks(nums: list[int]) -> int:
    if len(nums) <= 4:
        return -1
    first_loc_max_idx = second_loc_max_idx = 0
    ans = float('inf')
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            first_loc_max_idx, second_loc_max_idx = i, first_loc_max_idx
            if first_loc_max_idx and second_loc_max_idx:
                ans = min(ans, first_loc_max_idx - second_loc_max_idx)
    return ans if ans != float('inf') else -1


# print(min_distance_between_peaks([1, 3, 2, 5, 4, 1, 3, 2]))
# print(min_distance_between_peaks([1, 2, 3, 4, 5, 6, 7, 8]))
# print(min_distance_between_peaks([1]))
# print(min_distance_between_peaks([1, 2, 1]))
# print(min_distance_between_peaks([-1, 1, 0, 1, -1]))
