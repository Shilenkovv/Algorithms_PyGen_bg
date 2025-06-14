def have_common_element(nums1: list[int], nums2: list[int]) -> bool:
    p1, p2 = 0, 0

    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] == nums2[p2]:
            return True
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            p1 += 1
    return False


# print(have_common_element([1, 2, 3, 4], [2, 8, 16]))  # True
# print(have_common_element([-1, 0, 1], [0, 2]))  # True
# print(have_common_element([1, 3], [0, 2, 4, 8]))  # False
