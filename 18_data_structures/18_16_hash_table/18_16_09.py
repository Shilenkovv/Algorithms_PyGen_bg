from collections import Counter
from typing import List


def min_removals(nums1: List[int], nums2: List[int]) -> int:
    cntr1 = Counter(nums1)
    cntr2 = Counter(nums2)
    if len(nums1) > len(nums2):
        cntr1, cntr2 = cntr2, cntr1
    ans = 0

    for k in cntr1:
        if k in cntr2:
            ans += min(cntr1[k], cntr2[k])
    return ans
