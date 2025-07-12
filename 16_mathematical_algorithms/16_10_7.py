from typing import List


def prime_factors_in_factorial(n: int) -> list[int]:
    if n == 0 or n == 1:
        return []

    # Решето Эратосфена для поиска простых чисел до n
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    factors: List[int] = []
    for p in primes:
        # Считаем степень простого p в разложении n!
        exp = 0
        power = p
        while power <= n:
            exp += n // power
            power *= p
        factors.extend([p] * exp)

    return factors
