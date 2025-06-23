def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


def count_victories(power):
    right = 1
    rivals = -1

    while sum_of_squares(right) <= power:
        right *= 2

    left = right // 2

    while left <= right:
        middle = (left + right) // 2
        if sum_of_squares(middle) <= power:
            rivals = middle
            left = middle + 1
        else:
            right = middle - 1

    return rivals
