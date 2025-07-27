from collections import Counter
from typing import List


def unique(nums: List[int]) -> List[int]:
    cntr = Counter(nums)
    return [k for k in cntr if cntr[k] == 1]
