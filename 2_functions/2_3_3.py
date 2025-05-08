def get_quadrant(p: tuple[int, int]) -> int | None:
    """
    Определяет номер координатной четверти для заданной точки на плоскости.

    Точка задается в виде кортежа из двух целых чисел (x, y).
    Если точка лежит на одной из осей, возвращается None.

    Args:
        p (tuple[int, int]): Кортеж из двух целых чисел (x, y), где -10 <= x, y <= 10.

    Returns:
        int | None: Номер четверти (1, 2, 3 или 4) или None, если точка лежит на оси/осях.
    """
    if not isinstance(p, tuple) or len(p) != 2 or not all(isinstance(i, int) for i in p):
        raise ValueError('p должно быть кортежем из двух целых чисел')

    if any(num == 0 for num in p):
        return None
    if p[0] > 0 and p[1] > 0:
        return 1
    if p[0] < 0 and p[1] > 0:
        return 2
    if p[0] < 0 and p[1] < 0:
        return 3
    if p[0] > 0 and p[1] < 0:
        return 4
