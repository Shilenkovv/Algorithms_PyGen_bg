def is_power_of_three(n: int) -> bool:
    if n == 1:
        return True

    b = n
    cur_sum = 0
    while b:
        cur_sum += b % 10
        b //= 10
    if cur_sum % 3:
        return False

    a = 3

    while a <= n:
        if a == n:
            return True
        a *= 3
    return False


print(is_power_of_three(81))  # 3⁴ = 81 # True
print(is_power_of_three(9))  # 3² = 9 # True
print(is_power_of_three(6))  # False
print(is_power_of_three(1))  # True
print(is_power_of_three(243))  # True
print(is_power_of_three(729))  # True
print(is_power_of_three(728))
