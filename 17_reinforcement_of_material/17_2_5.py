from typing import List


def make_list_factors(num: int) -> List[int]:
    divisors: List[int] = []
    divisor = 2
    while divisor * divisor <= num:
        while num % divisor == 0:
            divisors.append(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        divisors.append(num)
    return divisors


def count_nums_with_k_prime_divisors(a: int, b: int, k: int) -> int:
    counter = 0
    while a <= b:
        if len(set(make_list_factors(a))) == k:
            counter += 1
        a += 1
    return counter


# print(count_nums_with_k_prime_divisors(1, 10, 2))  # 6, 10 # 2
