def count_squares(n: int, m: int) -> int:
    tot = 0
    m, n = max(m, n), min(m, n)
    while n != 0 and m != 0:
        tot += m // n
        m, n = n, m % n
    return tot


# print(count_squares(3, 15))  # 5
# print(count_squares(12, 8))  # 3
# print(count_squares(10, 3))  # 6
# print(count_squares(1000, 1))  # 1000
