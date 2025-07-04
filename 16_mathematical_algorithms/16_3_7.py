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


def count_digits_sum(num: int) -> int:
    if num <= 9:
        return num
    ans = 0
    while num != 0:
        ans += num % 10
        num //= 10
    return ans


def is_smith_num(num: int) -> bool:
    list_divisors = make_list_factors(num)
    if len(list_divisors) == 1:
        return False
    num_dig_sum = count_digits_sum(num)
    divisors_dig_sum = 0
    for elem in list_divisors:
        divisors_dig_sum += count_digits_sum(elem)
    return num_dig_sum == divisors_dig_sum


# print(is_smith_num(58))  # 2 * 29; 5 + 8 = 13, 2 + 2 + 9 = 13 # True
# print(is_smith_num(2))  # True
# print(is_smith_num(3))  # True
# print(is_smith_num(5))  # True
# print(is_smith_num(576))  # True
