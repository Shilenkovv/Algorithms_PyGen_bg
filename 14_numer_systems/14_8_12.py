from typing import List


def extra_num(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result
