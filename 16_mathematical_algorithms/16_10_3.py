def factorial_base(n: int) -> int:
    cur_fact = 1
    cur_num = 2

    while n >= cur_fact:
        cur_fact *= cur_num
        if cur_fact == n:
            return cur_num
        cur_num += 1
    return -1


print(factorial_base(6))  # 3! = 6
print(factorial_base(24))  # 4! = 24
print(factorial_base(30))  # -1
