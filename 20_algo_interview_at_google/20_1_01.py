from typing import List


def count_elements_with_both_bounds(nums: List[int]) -> int:
    min_elem = min(nums)
    max_elem = max(nums)

    n = 0
    for elem in nums:
        if elem != min_elem and elem != max_elem:
            n += 1
    return n
