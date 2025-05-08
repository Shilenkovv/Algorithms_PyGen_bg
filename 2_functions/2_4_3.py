def equation_of_line(values: list[int, int, int, int, int]) -> str | None:
    """
    Определяет уравнение прямой вида y = kx + b на основе значений функции
    в точках x = 0, 1, 2, 3, 4. Если уравнение невозможно определить, возвращает None.

    Args:
        values (list[int, int, int, int, int]): Список из пяти значений функции
            [y(0), y(1), y(2), y(3), y(4)], где:
            - y(0): Значение функции в точке x = 0.
            - y(1): Значение функции в точке x = 1.
            - y(2): Значение функции в точке x = 2.
            - y(3): Значение функции в точке x = 3.
            - y(4): Значение функции в точке x = 4.

    Returns:
        str | None: Уравнение прямой в строковом формате (например, 'y = 2x + 3')
        или None, если данные не соответствуют линейной функции.

    Raises:
        Exception: Если невозможно построить линейное уравнение из-за совпадения x-координат.
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

    k, b = linear_coefficients((0, values[0]), (1, values[1]))
    if k == 0 and b == 0:
        return 'y = 0'
    if not all([2 * k + b == values[2], 3 * k + b == values[3], 4 * k + b == values[4]]):
        return None
    ans_k = ''
    ans_b = ''
    ans = 'y = '
    if k == 1:
        ans_k = 'x'
    elif k == -1:
        ans_k = '-x'
    elif k != 0:
        ans_k = f'{int(k)}x'
    if ans_k:
        if b > 0:
            ans_b = f' + {int(b)}'
        elif b < 0:
            ans_b = f' - {int(abs(b))}'
    else:
        ans_b = f'{int(b)}'
    return ans + ans_k + ans_b
