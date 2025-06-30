from string import ascii_uppercase, digits
from typing import List


def is_double_base_palindrome(num: int, p: int) -> bool:
    DIGITS_LETTERS = digits + ascii_uppercase
    str_num = str(num)
    n = len(str_num)

    for i in range(n // 2):
        if str_num[i] != str_num[-1 - i]:
            return False
    str_base_num_list: List[str] = []

    while num != 0:
        last_digit = DIGITS_LETTERS[num % p]
        str_base_num_list.append(last_digit)
        num //= p
    m = len(str_base_num_list)
    for j in range(m // 2):
        if str_base_num_list[j] != str_base_num_list[-1 - j]:
            return False
    return True


print(is_double_base_palindrome(33, 2))  # True
print(is_double_base_palindrome(51, 2))  # False
print(is_double_base_palindrome(1, 5))  # True
print(is_double_base_palindrome(181, 10))  # True
print(is_double_base_palindrome(144, 3))  # False
