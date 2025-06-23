def solve(a: int, b: int, c: int) -> set:
    result = set()
    d = b**2 - 4 * a * c
    if d < 0:
        return result
    result.add((-b + d**0.5) / (2 * a))
    result.add((-b - d**0.5) / (2 * a))
    return result
