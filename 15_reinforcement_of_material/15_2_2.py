from typing import List


def oct_to_bin(oct_str: str) -> str:
    if oct_str == '0':
        return oct_str

    n: int = len(oct_str)
    num: int = 0

    for i in range(n - 1, -1, -1):
        num += int(oct_str[i]) * 8 ** (n - 1 - i)

    bin_num_list: List[str] = []
    while num != 0:
        last_digit = num % 2
        bin_num_list.append(str(last_digit))
        num //= 2

    return ''.join(list(reversed(bin_num_list))) if bin_num_list else '0'


print(oct_to_bin('1'))  # 1
print(oct_to_bin('0'))  # 0
print(oct_to_bin('14'))  # 1100
print(oct_to_bin('123'))  # 1010011
