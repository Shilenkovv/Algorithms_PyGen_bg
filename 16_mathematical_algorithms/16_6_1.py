from math import gcd


def simplify(a: int, b: int) -> str:
    return str(a // gcd(a, b)) + '/' + str(b // gcd(a, b))


print(simplify(3, 6))
