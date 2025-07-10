def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


# print(lcm(4, 16))  # 16
# print(lcm(1, 1))  # 1
# print(lcm(5, 6))  # 30
