from typing import Set


def make_all_divisors(num: int) -> Set[int]:
    divisors: Set[int] = set([1])
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            divisors.add(divisor)
            divisors.add(num // divisor)
        divisor += 1
    return divisors


def is_perfect_num(num: int) -> bool:
    if num == 1:
        return False
    sum_all_divisors = sum(make_all_divisors(num))
    return sum_all_divisors == num


# print(is_perfect_num(6))  # True
# print(is_perfect_num(28))  # True
# print(is_perfect_num(15))  # False
