def min_difference(nums1: list[int], nums2: list[int]) -> int:
    nums1.sort()
    nums2.sort()

    i, j = 0, 0
    min_diff = abs(nums1[i] - nums2[j])
    while i < len(nums1) and j < len(nums2):
        curr_diff = abs(nums1[i] - nums2[j])
        if curr_diff < min_diff:
            min_diff = curr_diff
            if min_diff == 0:
                return 0
        if nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1

    return min_diff


# print(min_difference([4, 1, 5], [8, 11, 9, 10]))  # (5, 8)
# print(min_difference([3, 2, 7, 5], [6, 4, 0]))  # (5, 6) # 1
# print(min_difference([6, 4, 5], [3, 1, 5, 8]))  # (5, 5) # 0
