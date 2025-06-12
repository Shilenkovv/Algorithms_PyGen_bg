import math


def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return math.comb(n, k)


def radix_sum(n):
    result = 0
    for k in range(13):  # k = 0..12
        sign = (-1) ** k
        term = comb(12, k) * comb(n - 10 * k + 11, 11)
        result += sign * term
    return result
