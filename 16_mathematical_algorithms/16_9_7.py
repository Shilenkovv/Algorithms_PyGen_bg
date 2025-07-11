def sum_of_twos(n: int) -> int:
    positive = 10 * (10**n - 1) // 9
    return 2 * (positive - n) // 9


# print(sum_of_twos(1))
# print(sum_of_twos(2))
# print(sum_of_twos(5))
