def bit_difference(num1: int, num2: int) -> int:
    # XOR покажет биты, которые отличаются
    diff = num1 ^ num2
    # Подсчёт количества установленных битов (различий)
    count = 0
    while diff:
        count += diff & 1
        diff >>= 1
    return count
