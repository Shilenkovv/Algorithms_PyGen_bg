from typing import List


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def super_gcd(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    cur_gcd = gcd(nums[1], nums[0])
    for i in range(2, len(nums)):
        cur_gcd = gcd(cur_gcd, nums[i])
    return cur_gcd


# print(super_gcd([8, 16, 12]))
