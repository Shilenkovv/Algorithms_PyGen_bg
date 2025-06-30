from typing import List


def max_xor_excluding_one(nums: List[int]) -> int:
    total_xor = 0
    for num in nums:
        total_xor ^= num

    max_xor = 0
    for num in nums:
        current_xor = total_xor ^ num
        if current_xor > max_xor:
            max_xor = current_xor

    return max_xor
