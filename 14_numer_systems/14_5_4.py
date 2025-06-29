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


def bin_to_oct(binary_str: str) -> str:
    bin2oct = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7',
    }
    ans: List[str] = []
    pointer: int = len(binary_str)

    while pointer > 0:
        start = pointer - 3 if pointer >= 3 else 0
        ans.append(bin2oct.get(binary_str[start:pointer].zfill(3), 'error'))
        pointer -= 3

    return ''.join(reversed(ans))


def hex_to_oct(hex_str: str) -> str:
    bin_str = hex_to_bin(hex_str)
    oct_str = bin_to_oct(bin_str)

    return oct_str


print(hex_to_oct('A'))  # 12
print(hex_to_oct('3C'))  # 74
print(hex_to_oct('AAA'))  # 5252
