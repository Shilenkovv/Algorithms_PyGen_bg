def bit_reverse(num: int) -> int:
    return int(bin(num).replace('0b', '')[::-1], 2)
