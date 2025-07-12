def double_factorial(n: int) -> int:
    if n == 0:
        return 1
    tot = 1
    start = 1 if n % 2 else 2

    for i in range(start, n + 1, 2):
        tot *= i
    return tot


print(double_factorial(0))  # 0!! = 1
print(double_factorial(1))  # 1!! = 1
print(double_factorial(2))  # 2!! = 2
print(double_factorial(4))  # 4!! = 2 * 4 = 8
print(double_factorial(5))  # 5!! = 1 * 3 * 5 = 15
print(double_factorial(6))  # 6!! = 2 * 4 * 6 = 48
