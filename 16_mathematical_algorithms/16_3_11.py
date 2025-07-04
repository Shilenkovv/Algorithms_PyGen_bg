from typing import Tuple


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def goldbach_pair(num: int) -> Tuple[int, int]:
    if num % 2 or num < 4:
        print('num should be even and greater than 3')
        return None
    for i in range(2, num // 2 + 1):
        if is_prime(i):
            if i == num - i:
                return (i, i)
            elif is_prime(num - i):
                return (i, num - i)
    else:
        return (-1, -1)


# print(goldbach_pair(4))  # (2, 2)
# print(goldbach_pair(8))  # (3, 5)
# print(goldbach_pair(18))  # (5, 13)
# print(goldbach_pair(10))  # (3, 7)
# print(goldbach_pair(14))  # (7, 7)
# print(goldbach_pair(9)) #
