def sum_powers_of_two(n: int, m: int) -> int:
    return (1 << n) + (1 << m)


print(sum_powers_of_two(2, 3))  # 12
