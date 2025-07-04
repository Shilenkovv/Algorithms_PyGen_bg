from typing import List


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


def special_primes(n: int, k: int) -> None:
    ans: List[int] = []

    for i in range(2, n + 1):
        if i % 10 != k:
            continue
        elif is_prime(i):
            ans.append(i)
    return ans


# print(special_primes(50, 7))
# print(special_primes(10, 2))
# print(special_primes(20, 4))
# delongi -
# melita mivona
