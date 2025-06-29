from string import ascii_uppercase, digits
from typing import List

DIGITS = digits + ascii_uppercase


def from_decimal(num: int, base: int) -> str:
    result: List[str] = []

    while num:
        last_digit = num % base
        result.append(DIGITS[last_digit])
        num //= base

    return ''.join(reversed(result))


print(from_decimal(11, 2))
print(from_decimal(1296, 36))
print(from_decimal(1, 16))
