from typing import List


def is_geometric(nums: List[int]) -> bool:
    if nums[1] == 0 or nums[0] == 0:
        return False
    q = nums[1] / nums[0]
    for i in range(1, len(nums) - 1):
        if nums[i] == 0 or nums[i + 1] == 0 or nums[i + 1] / nums[i] != q:
            return False
    return True
