def max_of_two(a: int, b: int) -> int:
    if a < b:
        return b
    return a


def max_of_four(a: int, b: int, c: int, d: int) -> int:
    return max_of_two(max_of_two(a, b), max_of_two(c, d))
