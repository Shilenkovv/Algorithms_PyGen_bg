from typing import Tuple


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def closest_primes(a: int, b: int) -> int | Tuple[int, int]:
    first_found_s_num = 1
    second_found_s_num = 1

    min_diff = float('inf')
    ans: int | Tuple[int, int] = -1

    for i in range(a, b + 1):
        if is_prime(i):
            if first_found_s_num == 1:
                first_found_s_num = i
            else:
                first_found_s_num, second_found_s_num = i, first_found_s_num
                cur_diff = first_found_s_num - second_found_s_num
                if cur_diff == 1:
                    return (second_found_s_num, first_found_s_num)
                elif cur_diff < min_diff:
                    min_diff = first_found_s_num - second_found_s_num
                    ans = (second_found_s_num, first_found_s_num)

    return ans


# print(closest_primes(10, 20)) # (11, 13)
# print(closest_primes(100, 120))  # (101, 103)
