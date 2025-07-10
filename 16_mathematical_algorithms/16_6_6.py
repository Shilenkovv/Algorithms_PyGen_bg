import math


def find_pair(gcd, lcm):
    if lcm % gcd != 0:
        return -1
    k = lcm // gcd
    for x in range(1, int(math.isqrt(k)) + 1):
        if k % x == 0:
            y = k // x
            if math.gcd(x, y) == 1:
                a, b = gcd * x, gcd * y
                return tuple(sorted((a, b)))
    return -1
