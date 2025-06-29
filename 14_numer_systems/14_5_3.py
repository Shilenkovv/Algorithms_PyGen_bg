from typing import List


def oct_to_hex(oct_str: str) -> str:
    oct2bin = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
    }

    bin2hex = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F',
    }

    ans_binary: List[str] = []

    for i in range(len(oct_str) - 1, -1, -1):
        ans_binary.append(oct2bin.get(oct_str[i], 'error'))

    if ans_binary[-1] == '000':
        ans_binary[-1] = '0'
    else:
        ans_binary[-1] = ans_binary[-1].lstrip('0')

    bin_str = ''.join(reversed(ans_binary))

    ans_hex: List[str] = []
    pointer = len(bin_str)

    while True:
        start = max(0, pointer - 4)
        ans_hex.append(bin2hex.get(bin_str[start:pointer].zfill(4), 'error'))
        pointer -= 4
        if pointer <= 0:
            break

    return ''.join(reversed(ans_hex))


# print(oct_to_hex('12'))  # A
# print(oct_to_hex('74'))  # 3C
# print(oct_to_hex('0'))  # 0
