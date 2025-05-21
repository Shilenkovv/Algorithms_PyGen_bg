def get_argument(func, value):
    if func(0) == value:
        return 0
    elif func(0) < value:
        right = 1
        while func(right) < value:
            right *= 2
        left = right // 2
    else:
        left = -1
        while func(left) > value:
            left *= 2
        right = left // 2
    while left < right:
        mid = left + (right - left) // 2
        if func(mid) == value:
            return mid
        elif func(mid) > value:
            right = mid
        else:
            left = mid + 1
    return None


# def func(x):
#     return x**3 + 1


# print(get_argument(func, 28))  # f(3) = 28


# def func(x):
#     return 2**x - 5


# print(get_argument(func, -4))  # f(0) = -4


# def func(x):
#     return 2 * x**5 - 100


# print(get_argument(func, 15452))  # f(6) = 15452


# def func(x):
#     return 22 * x - 200


# print(get_argument(func, 86))  # f(13) = 86
