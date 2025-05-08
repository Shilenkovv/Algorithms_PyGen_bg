def intersections(a: int, b: int, c: int, k: int, m: int) -> set:
    """
    Finds the intersection points of a parabola (ax^2 + bx + c = 0)
    with a line (y = kx + m).

    Args:
        a (int): Coefficient of x^2 in the quadratic equation.
        b (int): Coefficient of x in the quadratic equation.
        c (int): Constant term in the quadratic equation.
        k (int): Slope of the line.
        m (int): Intercept of the line.

    Returns:
        set: A set of intersection points as tuples (x, y). If no intersection, returns an empty set.
    """
    b -= k
    c -= m
    x_set = set()
    if b == 0 and c == 0:
        x_set.add(0.0)
    elif b == 0 and ((c > 0 and a < 0) or (c < 0 and a > 0)):
        return set()
    elif b == 0:
        x_set.add(abs(c) ** 0.5)
        x_set.add(-(abs(c) ** 0.5))
    elif c == 0:
        x_set.add(-(b / a))
        x_set.add(0.0)
    else:
        d = b**2 - 4 * a * c
        if d < 0:
            return set()
        elif d == 0:
            x_set.add(-(b / (2 * a)))
        else:
            x_set.add(-(b + d**0.5) / (2 * a))
            x_set.add(-(b - d**0.5) / (2 * a))
    result = set()
    for elem in x_set:
        result.add((elem, elem * k + m))
    return result
