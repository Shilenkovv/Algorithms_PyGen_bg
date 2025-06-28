from typing import List


def create_number(digits: List[int]) -> int:
    ans = 0
    n = len(digits)
    for i in range(n):
        ans += digits[n - 1 - i] * 10**i
    return ans


print(create_number([2, 3, 8, 4]))  # 2384
