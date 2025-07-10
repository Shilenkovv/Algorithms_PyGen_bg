from typing import Tuple


def split_into_sum(n: int) -> Tuple[int, int]:
    max_divisor: int = 1  # минимальный делитель, который всегда подходит
    i = 1
    while i * i <= n:
        if n % i == 0:
            # i — делитель
            if i < n and i > max_divisor:
                max_divisor = i
            # n // i — парный делитель
            other = n // i
            if other < n and other > max_divisor:
                max_divisor = other
        i += 1
    a, b = max_divisor, n - max_divisor
    return tuple([a, b]) if a <= b else tuple([b, a])


# print(split_into_sum(5))
