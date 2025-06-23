def polynomial_creator(p: tuple):
    return lambda x: sum(coeff * x ** (len(p) - i - 1) for i, coeff in enumerate(p))
