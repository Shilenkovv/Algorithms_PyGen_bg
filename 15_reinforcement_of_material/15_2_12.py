def super_xor(n: int) -> int:
    remainder = n % 4
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n + 1
    else:  # remainder == 3
        return 0
