def rightmost_set_bit(num: int) -> int:
    position = 0
    while num > 0:
        if num & 1:
            return position
        num >>= 1
        position += 1
