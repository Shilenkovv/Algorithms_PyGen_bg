from typing import List


def bin_to_hex(bin_str: str) -> str:
    n: int = len(bin_str)
    num: int = 0

    for i in range(n - 1, -1, -1):
        num += int(bin_str[i]) * 2 ** (n - 1 - i)

    hex_letters: List[str] = ['A', 'B', 'C', 'D', 'E', 'F']

    hex_num_list: List[str] = []
    while num != 0:
        last_digit = num % 16
        if last_digit <= 9:
            hex_num_list.append(str(last_digit))
        else:
            hex_num_list.append(hex_letters[last_digit - 10])
        num //= 16

    return ''.join(list(reversed(hex_num_list))) if hex_num_list else '0'


# print(bin_to_hex('0'))  # 0
# print(bin_to_hex('1'))  # 1
# print(bin_to_hex('1011'))  # B
# print(bin_to_hex('101111'))  # 2F
