def max_power_of_two_divisor(num: int) -> int:
    # Выделяем младший установленный бит
    power_of_two = num & (-num)
    # Находим показатель степени двойки (количество сдвигов вправо)
    exponent = 0
    while power_of_two > 1:
        power_of_two >>= 1
        exponent += 1
    return 2**exponent
