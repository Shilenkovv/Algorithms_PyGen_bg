from math import gcd


def fibonacci(n: int) -> int:
    prev, cur = 1, 1
    for _ in range(n - 2):
        prev, cur = cur, prev + cur
    return cur


def gcd_of_fibonacci(n: int, m: int) -> int:
    return fibonacci(gcd(n, m))


print(gcd_of_fibonacci(20, 30))
