def quadratic_intersections(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int) -> set:
    a = a1 - a2
    b = b1 - b2
    c = c1 - c2
    final_result = set()

    def solve(a: int, b: int, c: int) -> set:
        result = set()
        if a == 0:
            if b != 0:
                result.add(-1 * (c / b))
                return result
            else:
                return result
        if b == 0:
            if c == 0:
                return {0.0}
            elif c < 0:
                return {(-c / a) ** 0.5, -((-c / a) ** 0.5)}
            else:
                return result
        d = b**2 - 4 * a * c
        if d < 0:
            return result
        if a != 0:
            x_cur_1 = (-b + d**0.5) / (2 * a)
            x_cur_1 = 0.0 if x_cur_1 == 0 else x_cur_1
            x_cur_2 = (-b - d**0.5) / (2 * a)
            x_cur_2 = 0.0 if x_cur_2 == 0 else x_cur_2
            result.add(x_cur_1)
            result.add(x_cur_2)
        return result

    x_list = solve(a, b, c)
    if x_list:
        for x in x_list:
            final_result.add((x, a1 * x**2 + b1 * x + c1))
        return final_result
    return set()


# print(quadratic_intersections(2, -4, 2, 4, 0, 2))
# print(quadratic_intersections(2, 2, 5, 2, 2, 1))
