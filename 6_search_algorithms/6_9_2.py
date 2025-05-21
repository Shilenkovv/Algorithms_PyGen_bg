import numpy as np


def func(a: float, x: float) -> float:
    # return 2**x + x**0.5 - a
    return np.log2(a - np.pow(x, 0.5)) - x


def solve_equation(a: float) -> float:
    left = 0
    right = a
    epsilon = 0.000001

    while right - left > epsilon:
        mid = left + (right - left) / 2
        if func(a, mid) < 0:
            right = mid
        else:
            left = mid

    return round(left, 6)
