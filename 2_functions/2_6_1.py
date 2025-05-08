def quadratic_values(a: int, b: int, c: int, start: int = 0, step: int = 1) -> list:
    result = [(x, a * x**2 + b * x + c) for x in range(start, start + 10 * step, step)]
    return result
