def func(x: float, a: float, b: float, c: float, d: float) -> float:
    return a * x**3 + b * x**2 + c * x + d


def solve_equation(a: float, b: float, c: float, d: float) -> float:
    if a < 0:
        a, b, c, d = -a, -b, -c, -d

    left, right = -1, 1

    while func(left, a, b, c, d) > 0:
        left *= 2

    while func(right, a, b, c, d) < 0:
        right *= 2

    epsilon = 0.000001

    while right - left > epsilon:
        middle = (left + right) / 2

        if func(middle, a, b, c, d) < 0:
            left = middle
        else:
            right = middle

    return left


# print(solve_equation(1, -3, 3, -1)) # 1
# print(solve_equation(-1, -6, -12, -7)) # -1
# print(solve_equation(1, 3, -2, 8)) # -4
