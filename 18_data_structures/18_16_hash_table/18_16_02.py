from collections import Counter
from typing import List, Tuple


def min_max_freq(nums: List[int]) -> Tuple[int, int]:
    cntr: dict[int, int] = Counter(nums)
    min_cnt = float('inf')
    max_cnt = -float('inf')

    for k, v in cntr.items():
        if v < min_cnt:
            min_key: int = k
            min_cnt: int = v
        elif v == min_cnt and k < min_key:
            min_key = k
        if v > max_cnt:
            max_key = k
            max_cnt = v
        elif v == max_cnt and k < max_key:
            max_key = k
    return (min_key, max_key)
