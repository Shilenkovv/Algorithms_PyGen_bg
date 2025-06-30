def is_power_of_two(num: int) -> int:
    return num > 0 and (num & (num - 1)) == 0
