from typing import List


def sum_shaded_area(matrix: List[List[int]]) -> int:
    n = len(matrix)
    mid = n // 2  # Центр матрицы (индекс)
    total = 0

    for i in range(n):
        # Определяем начало и конец диапазона индексов закрашенной области для строки i
        start = max(0, mid - i)
        end = min(n, mid + i + 1)
        if i > mid:
            start = i - mid
            end = n - (i - mid)
        # Суммируем элементы строки в закрашенной области
        total += sum(matrix[i][start:end])

    return total
