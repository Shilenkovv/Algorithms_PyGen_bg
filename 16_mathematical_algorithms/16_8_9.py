def even_odd_sum_difference(a: int, b: int) -> int:
    n = b - a + 1
    odd_n, even_n = n // 2, n // 2
    first_odd = True if a % 2 else False
    if first_odd:
        odd_n += n % 2
    else:
        even_n += n % 2
    if first_odd:
        odd_sum = ((2 * a + 2 * (odd_n - 1)) * odd_n) // 2
        even_sum = ((2 * (a + 1) + 2 * (even_n - 1)) * even_n) // 2
    else:
        odd_sum = ((2 * (a + 1) + 2 * (odd_n - 1)) * odd_n) // 2
        even_sum = ((2 * a + 2 * (even_n - 1)) * even_n) // 2
    return even_sum - odd_sum


# print(even_odd_sum_difference(1, 5))  # (2 + 4) - (1 + 3 + 5) = -3
# print(even_odd_sum_difference(2, 6))  # (2 + 4 + 6) - (3 + 5) = 4
# print(even_odd_sum_difference(5, 6))  # 6 - 5 = 1
# print(even_odd_sum_difference(1, 1))  # 0 - 1 = -1
# print(even_odd_sum_difference(8, 15))  # (8 + 10 + 12 + 14) - (9 + 11 + 13 + 15) = -4
