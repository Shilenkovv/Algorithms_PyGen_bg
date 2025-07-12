def count_arrangements(n: int) -> int:
    # Решето Эратосфена для подсчёта количества простых чисел до n
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    prime_count = sum(sieve)

    from math import factorial

    return factorial(prime_count) * factorial(n - prime_count)
