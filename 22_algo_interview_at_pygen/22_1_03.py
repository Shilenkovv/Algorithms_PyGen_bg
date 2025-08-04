from typing import List


def sum_of_mid_elements(nums1: List[int], nums2: List[int]) -> int:
    first = 0
    second = 0
    new_list: List[int] = []
    n = len(nums1)

    while first < len(nums1) and second < len(nums2):
        if nums1[first] < nums2[second]:
            new_list.append(nums1[first])
            first += 1
        else:
            new_list.append(nums2[second])
            second += 1
        if len(new_list) == n + 1:
            return new_list[-1] + new_list[-2]

    while first < len(nums1):
        new_list.append(nums1[first])
        first += 1
        if len(new_list) == n + 1:
            return new_list[-1] + new_list[-2]
    while second < len(nums2):
        new_list.append(nums2[second])
        second += 1
        if len(new_list) == n + 1:
            return new_list[-1] + new_list[-2]


# print(sum_of_mid_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]  7
# print(sum_of_mid_elements([1, 2, 3], [1, 2, 3]))  # [1, 1, 2, 2, 3, 3] 4
# print(sum_of_mid_elements([1, 3, 5, 7], [2, 4, 6, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8] 9
# print(sum_of_mid_elements([1], [2]))  # [1, 2] 3
# print(sum_of_mid_elements([-3, -2, -1], [1, 2, 3]))  # [-3, -2, -1, 1, 2, 3] 0
# print(sum_of_mid_elements([1, 1, 1], [1, 1, 1]))  # [1, 1, 1, 1, 1, 1] 2
