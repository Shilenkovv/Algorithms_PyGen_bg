def interesting_primes(n: int):
    # Решето Эратосфена
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    def has_no_zero(num: int) -> bool:
        return '0' not in str(num)

    def all_truncations_prime(num: int) -> bool:
        s = str(num)
        # Проверяем все варианты с удалением ведущих цифр
        for i in range(len(s)):
            if not is_prime[int(s[i:])]:
                return False
        return True

    count = 0
    for num in range(2, n + 1):
        if is_prime[num] and has_no_zero(num) and all_truncations_prime(num):
            count += 1

    return count


# print(interesting_primes(50))  # 10
