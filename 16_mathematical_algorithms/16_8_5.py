def is_triangle_num(num: int) -> bool:
    n = 0
    add = 1
    while n < num:
        n += add
        add += 1
    if n == num:
        return True
    return False


print(is_triangle_num(10))  # True
print(is_triangle_num(1))  # True
print(is_triangle_num(5))  # False
print(is_triangle_num(3))  # True
