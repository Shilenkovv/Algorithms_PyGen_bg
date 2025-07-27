from typing import List


def index_mapping(nums1: List[int], nums2: List[int]) -> List[int]:
    idx_dict = {nums2[i]: i for i in range(len(nums2))}
    ans = [idx_dict[nums1[i]] for i in range(len(nums1))]

    return ans
