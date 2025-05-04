def on_one_line(p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]) -> bool:
    """
    Проверяет, лежат ли три точки на одной прямой.

    Args:
        p1 (tuple[int, int]): Координаты первой точки (x1, y1).
        p2 (tuple[int, int]): Координаты второй точки (x2, y2).
        p3 (tuple[int, int]): Координаты третьей точки (x3, y3).

    Returns:
        bool: True, если все три точки лежат на одной прямой, иначе False.

    Raises:
        Exception: Если невозможно построить линейное уравнение для первых двух точек (например, если они образуют вертикальную линию).
    """

    def linear_coefficients(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[float, float]:
        """
        Вычисляет коэффициенты линейного уравнения y = kx + b, проходящего через две заданные точки.

        Args:
            p1 (tuple[int, int]): Координаты первой точки (x1, y1).
            p2 (tuple[int, int]): Координаты второй точки (x2, y2).

        Returns:
            tuple[float, float]: Кортеж, содержащий коэффициенты (k, b), где:
                k (float): Наклон линии (угловой коэффициент).
                b (float): Смещение линии (свободный член).

        Raises:
            Exception: Если x-координаты точек совпадают (x1 == x2), что делает построение вертикальной прямой невозможным.
        """

        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            raise Exception('Невозможно построить вертикальную прямую линейной функцией.')
        k = (y2 - y1) / (x2 - x1)
        b = (x2 * y1 - x1 * y2) / (x2 - x1) if (x2 * y1 - x1 * y2) != 0 else 0.0
        return (k, b)

    k, b = linear_coefficients(p1, p2)
    return p3[0] * k + b == p3[1]
