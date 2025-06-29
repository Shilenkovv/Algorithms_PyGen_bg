def convert_base(str_num: str, from_base: int, to_base: int) -> str:
    from string import ascii_uppercase, digits
    from typing import List

    if from_base == to_base:
        return str_num
    if str_num == '0':
        return '0'

    DIGITS = digits + ascii_uppercase
    result: List[str] = []
    num_base_10: int = 0
    n = len(str_num)

    for i in range(n - 1, -1, -1):
        num_base_10 += DIGITS.index(str_num[i]) * from_base ** (n - 1 - i)

    if to_base == 10:
        return str(num_base_10)

    while num_base_10 != 0:
        last_digit = num_base_10 % to_base
        result.append(DIGITS[last_digit])
        num_base_10 //= to_base

    return ''.join(reversed(result))


# print(convert_base('11100', 2, 10))  # 28
# print(convert_base('33', 10, 3))  # 1020
# print(convert_base('113', 7, 16))  # 3B
# print(convert_base('759375', 10, 15))  # 100000
