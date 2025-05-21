def func(x: float) -> float:
    return x**3


def cube_root(num: int) -> float:
    left = 0
    right = num
    epsilon = 0.000001
    while right - left > epsilon:
        mid = left + (right - left) / 2
        if func(mid) > num:
            right = mid
        else:
            left = mid
    return round(mid, 6)


# print(cube_root(8))
# print(cube_root(125))
# print(cube_root(100))
# print(cube_root(1))
# print(cube_root(10**8))
