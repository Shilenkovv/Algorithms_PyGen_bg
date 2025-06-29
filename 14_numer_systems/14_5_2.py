from typing import List


def hex_to_bin(hex_str: str) -> str:
    hex2bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    ans: List[str] = []

    for i in range(len(hex_str) - 1, -1, -1):
        ans.append(hex2bin.get(hex_str[i], 'error'))

    if ans[-1] == '0000':
        ans[-1] = '0'
    else:
        ans[-1] = ans[-1].lstrip('0')

    return ''.join(reversed(ans))


# print(hex_to_bin('1'))  # 1
# print(hex_to_bin('B'))  # 1010
# print(hex_to_bin('2F'))  # 101111
# print(hex_to_bin('AAA'))  # 101010101010
