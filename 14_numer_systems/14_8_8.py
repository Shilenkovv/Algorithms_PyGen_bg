def left_cyclic_shift(num: int, k: int) -> int:
    shifted = ((num << k) & 0xFF) | (num >> (8 - k))
    return shifted
