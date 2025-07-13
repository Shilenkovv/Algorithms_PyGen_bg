from typing import List


def count_ones_in_prime_binary_sequence(n: int) -> int:
    # Решето Эратосфена
    n_primes = 100000
    is_prime: List[bool] = [True] * (n_primes + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n_primes**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n_primes + 1, i):
                is_prime[j] = False

    tot_ones = 0
    tot_cnt = 0

    for i in range(len(is_prime)):
        if is_prime[i]:
            str_num_list: List[str] = []
            while i != 0:
                str_num_list.append(str(i % 2))
                i //= 2
            str_num = ''.join(reversed(str_num_list))

            for dig in str_num:
                tot_cnt += 1
                if dig == '1':
                    tot_ones += 1
                if tot_cnt == n:
                    return tot_ones


# print(count_ones_in_prime_binary_sequence(5))
