def shift_by_one_in_spiral_order(matrix):
    n, m = len(matrix), len(matrix[0])

    # Извлечение элементов матрицы по спирали
    spiral = []
    top, bottom, left, right = 0, n - 1, 0, m - 1

    while top <= bottom and left <= right:
        # Верхний ряд слева направо
        for col in range(left, right + 1):
            spiral.append(matrix[top][col])
        top += 1

        # Правый столбец сверху вниз
        for row in range(top, bottom + 1):
            spiral.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Нижний ряд справа налево
            for col in range(right, left - 1, -1):
                spiral.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Левый столбец снизу вверх
            for row in range(bottom, top - 1, -1):
                spiral.append(matrix[row][left])
            left += 1

    # Смещение элементов спирали на 1 позицию вправо
    spiral = [spiral[-1]] + spiral[:-1]

    # Запись элементов обратно в матрицу по спирали
    top, bottom, left, right = 0, n - 1, 0, m - 1
    idx = 0

    while top <= bottom and left <= right:
        # Верхний ряд слева направо
        for col in range(left, right + 1):
            matrix[top][col] = spiral[idx]
            idx += 1
        top += 1

        # Правый столбец сверху вниз
        for row in range(top, bottom + 1):
            matrix[row][right] = spiral[idx]
            idx += 1
        right -= 1

        if top <= bottom:
            # Нижний ряд справа налево
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = spiral[idx]
                idx += 1
            bottom -= 1

        if left <= right:
            # Левый столбец снизу вверх
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = spiral[idx]
                idx += 1
            left += 1


# Пример использования
matrix = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9],
]

shift_by_one_in_spiral_order(matrix)
print(*matrix, sep='\n')
