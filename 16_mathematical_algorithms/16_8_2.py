from typing import List


def is_arithmetic(nums: List[int]) -> bool:
    d = nums[1] - nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + d:
            return False
    return True
