from typing import List


def count_good_numbers(nums: List[int]) -> int:
    ans: int = 0
    BASE: int = 16

    for num in nums:
        eight_found: bool = False
        digits_cnt: int = 0
        n: int = num

        while n != 0 and not eight_found:
            if n % 10 == 8:
                eight_found = True
            n //= 10
        if not eight_found:
            continue
        while num != 0:
            last_digit = num % BASE
            if not digits_cnt and last_digit != 4:
                break
            digits_cnt += 1
            num //= BASE
            if digits_cnt >= 3:
                ans += 1
                break

    return ans


# print(count_good_numbers([1284, 5, 67, 2077, 6852]))
# print(count_good_numbers([8, 16]))  # 0
