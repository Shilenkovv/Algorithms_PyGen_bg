from math import factorial


def sum_of_digits_factorials(n: int) -> int:
    if n == 0:
        return 1
    tot = 0
    while n != 0:
        tot += factorial(n % 10)
        n //= 10
    return tot


print(sum_of_digits_factorials(214))  # 27
print(sum_of_digits_factorials(2003))  # 10
