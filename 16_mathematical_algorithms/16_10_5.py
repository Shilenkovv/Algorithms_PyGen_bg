from math import floor, log10


def count_digits_in_factorial(n: int) -> int:
    tot = 0
    for i in range(1, n + 1):
        tot += log10(i)
    return floor(tot) + 1


# print(count_digits_in_factorial(5))
# print(count_trailing_zeroes_in_factorial(4))  # 0
# print(count_trailing_zeroes_in_factorial(5))  # 1
# print(count_trailing_zeroes_in_factorial(10))  # 10! = 3628800 # 2
# print(count_trailing_zeroes_in_factorial(15))  # 15! = 1307674368000 # 3
