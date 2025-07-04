from typing import List, Set


def count_factors(num: int) -> int:
    divisors: Set[int] = set()
    divisor = 2
    while divisor * divisor <= num:
        while num % divisor == 0:
            divisors.add(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        return len(divisors) + 1
    return len(divisors)


def num_with_max_prime_divisors(nums: List[int]) -> int:
    max_divisors = -1
    ans = -1
    for elem in nums:
        cur_factors = count_factors(elem)
        if cur_factors > max_divisors:
            max_divisors = cur_factors
            ans = elem
        elif cur_factors == max_divisors and elem < ans:
            ans = elem
    return ans


# print(num_with_max_prime_divisors([24, 3, 4, 7, 30, 6]))
