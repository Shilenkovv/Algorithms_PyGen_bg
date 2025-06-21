def intersection_of_three_lists(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    ans = []
    p1, p2, p3 = 0, 0, 0

    while p1 < len(nums1) and p2 < len(nums2) and p3 < len(nums3):
        if all([nums1[p1] == nums2[p2] == nums3[p3]]):
            ans.append(nums1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        else:
            max_elem = max(nums1[p1], nums2[p2], nums3[p3])
            if nums1[p1] != max_elem:
                p1 += 1
            if nums2[p2] != max_elem:
                p2 += 1
            if nums3[p3] != max_elem:
                p3 += 1
    return ans


# print(intersection_of_three_lists([1, 2, 3, 4, 5], [1, 3, 5], [3, 4, 5])) # [3, 5]
# print(intersection_of_three_lists([1, 3], [4], [7, 8, 9]))  # []
# print(intersection_of_three_lists([0, 1, 2], [-1, 0, 1], [-2, -1, 0]))  # [0]
