def count_zeros(matrix: list[list[int]]):
   n = len(matrix)
    count = 0
    row, col = 0, n - 1  # Начинаем с первой строки и последнего столбца

    while row < n and col >= 0:
        if matrix[row][col] == 0:
            # Если элемент равен 0, добавляем все элементы выше в этом столбце
            count += col + 1
            row += 1  # Переходим к следующей строке
        else:
            # Если элемент равен 1, перемещаемся влево
            col -= 1

    return count


matrix = [[0, 0, 1],
          [1, 1, 1],
          [0, 1, 1]]

print(row_with_max_ones(matrix))
