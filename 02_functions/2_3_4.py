def is_point_in_rectangle(p: tuple[int, int], rect: list[tuple[int, int], tuple[int, int]]) -> bool:
    """
    Определяет, находится ли точка строго внутри прямоугольника.

    Точка задается в виде кортежа из двух целых чисел (x, y).
    Прямоугольник задается как список из двух кортежей (x1, y1) и (x2, y2),
    где (x1, y1) — левая нижняя вершина, а (x2, y2) — правая верхняя вершина.

    Args:
        p (tuple[int, int]): Кортеж из двух целых чисел (x, y), где -10 <= x, y <= 10.
        rect (list[tuple[int, int], tuple[int, int]]): Список двух кортежей из двух целых чисел.
    Returns:
        bool: True, если точка p лежит строго внутри прямоугольника rect (не на его границе),
        иначе False.
    """
    if (
        not isinstance(p, tuple)
        or len(p) != 2
        or not all(isinstance(i, int) for i in p)
        or len(rect) != 2
        or not isinstance(rect, list)
        or not all(isinstance(i, int) for i in rect[0])
        or not all(isinstance(i, int) for i in rect[1])
    ):
        raise ValueError('p должно быть кортежем из двух целых чисел')

    if all([p[0] > rect[0][0], p[0] < rect[1][0], p[1] > rect[0][1], p[1] < rect[1][1]]):
        return True
    return False
