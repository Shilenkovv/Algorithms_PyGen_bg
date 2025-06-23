def sort_each_diagonal(matrix: list[list[int]]):
    n = len(matrix)

    # Функция для получения элементов диагонали с заданной разницей индексов row - col
    def get_diagonal_elements(matrix, diff):
        return [matrix[row][col] for row in range(n) for col in range(n) if row - col == diff]

    # Функция для установки элементов на диагональ с заданной разницей индексов row - col
    def set_diagonal_elements(matrix, diff, sorted_diagonal):
        idx = 0
        for row in range(n):
            for col in range(n):
                if row - col == diff:
                    matrix[row][col] = sorted_diagonal[idx]
                    idx += 1

    # Обрабатываем диагонали с разницей индексов от -(n-1) до (n-1)
    for diff in range(-(n - 1), n):
        diagonal = get_diagonal_elements(matrix, diff)
        diagonal.sort()
        set_diagonal_elements(matrix, diff, diagonal)


# Пример использования
matrix = [[3, 7, 1], [2, 9, 4], [8, 1, 3]]

sort_each_diagonal(matrix)
print(*matrix, sep='\n')
