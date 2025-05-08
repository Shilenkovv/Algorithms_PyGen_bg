def polynomial_product(p1: tuple, p2: tuple) -> str:
    c1 = tuple(reversed(p1))
    c2 = tuple(reversed(p2))

    powers_dict = dict()

    for i, cur_c1 in enumerate(c1):
        for j, cur_c2 in enumerate(c2):
            cur_coef = powers_dict.setdefault(i + j, 0)
            cur_coef += cur_c1 * cur_c2
            powers_dict[i + j] = cur_coef
    ans = tuple(powers_dict.get(i) for i in sorted(powers_dict, reverse=True))
    return ans
