from math import gcd, lcm
from typing import List, Tuple


def sum_of_fractions(fractions: List[Tuple[int, int]]) -> Tuple[int, int]:
    if len(fractions) == 1:
        den = fractions[0][1]
    else:
        den = lcm(fractions[1][1], fractions[0][1])
    for i in range(2, len(fractions)):
        den = lcm(fractions[i][1], den)
    num = 0
    for fraction in fractions:
        num += fraction[0] * den // fraction[1]

    cur_gcd = gcd(den, num)
    while cur_gcd != 1:
        num //= cur_gcd
        den //= cur_gcd
        cur_gcd = gcd(den, num)
    return (num, den)


# print(sum_of_fractions([(1, 2), (1, 12), (3, 4)]))
# print(sum_of_fractions([(2, 4), (4, 12), (3, 9)]))
# print(sum_of_fractions([(1, 1), (5, 5)]))
# print(sum_of_fractions([(5, 10)]))
