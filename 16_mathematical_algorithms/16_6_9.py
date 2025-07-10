from math import gcd, sqrt
from typing import List


def count_pairs(n: int) -> int:
    # 1. Найти делители
    divisors: List[int] = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()

    count = 0
    length = len(divisors)

    # 2. Перебор пар (a, b)
    for i in range(length):
        a = divisors[i]
        for j in range(i + 1, length):
            b = divisors[j]
            if a * b > n:
                # Так как список отсортирован, дальше умножение будет только больше
                break
            if gcd(a, b) == 1:
                count += 1

    return count


# print(count_pairs(11))  #  (1, 11) # 1
# print(count_pairs(10)) # 4
