from typing import List


def min_sum_of_products(nums1: List[int], nums2: List[int]) -> int:
    ans = 0
    nums1.sort()
    nums2.sort(reverse=True)

    for elem1, elem2 in zip(nums1, nums2):
        ans += elem1 * elem2
    return ans


# print(min_sum_of_products([2, 6, 4], [3, 1, 5]))
