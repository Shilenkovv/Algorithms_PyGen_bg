from typing import List


def set_last_reset_bit(num: int) -> int:
    binary_num: List[str] = []
    while num != 0:
        binary_num.append(str(num % 2))
        num //= 2
    binary_num.reverse()

    for i in range(len(binary_num) - 1, -1, -1):
        if binary_num[i] == '0':
            binary_num[i] = '1'
            break
    else:
        binary_num = ['1'] + binary_num
    return int('0b' + ''.join(binary_num), 2)


print(bin(set_last_reset_bit(0b1)))
print(bin(set_last_reset_bit(0b10011)))
