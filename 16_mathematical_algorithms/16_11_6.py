def fibonacci(n: int) -> int:
    def fib_fast_doubling(k: int) -> tuple[int, int]:
        if k == 0:
            return (0, 1)
        a, b = fib_fast_doubling(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    # По условию F(1) = 1, F(2) = 1, но в формуле F(0) = 0
    # Поэтому для n >= 1 возвращаем первый элемент пары для n
    return fib_fast_doubling(n)[0]
