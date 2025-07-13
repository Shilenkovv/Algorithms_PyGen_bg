def count_lucky_numbers(a: int, b: int) -> int:
    # Решето Эратосфена
    is_prime = [True] * (b + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(b**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, b + 1, i):
                is_prime[j] = False
    counter = 0

    for i in range(a, b + 1):
        if is_prime[i] and '13' not in str(i):
            counter += 1
    return counter


# print(count_lucky_numbers(11, 20))  # 11, 13, 17 # 3
# print(count_lucky_numbers(113, 131))  # 127 # 1
# print(count_lucky_numbers(32, 36))  # 0
# print(count_lucky_numbers(13, 16))  # 0
# print(count_lucky_numbers(13, 17))  # 17 # 1
