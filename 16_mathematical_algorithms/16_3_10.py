def is_almost_prime(num: int) -> bool:
    counter = 0
    i = 2
    while i * i <= num:
        if num % i == 0:
            counter += 1
            if counter > 2:
                return False
            while num % i == 0:
                num //= i
        i += 1
    if num > 1:
        counter += 1
    return counter == 2


print(is_almost_prime(6))  # True
print(is_almost_prime(18))  # True
print(is_almost_prime(25))  # False
print(is_almost_prime(30))  # False
print(is_almost_prime(1))  # False
print(is_almost_prime(2))  # False
