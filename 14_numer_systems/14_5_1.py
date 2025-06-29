from typing import List


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


print(bin_to_oct('11'))  # 10
