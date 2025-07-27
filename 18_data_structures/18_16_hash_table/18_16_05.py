from typing import List


def has_double_pair(nums: List[int]) -> bool:
    seen: set[int] = set()
    for num in nums:
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False
