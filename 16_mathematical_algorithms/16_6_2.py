def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def euler_function(n: int) -> int:
    return sum([1 for i in range(1, n + 1) if gcd(i, n) == 1])


# print(euler_function(36))
