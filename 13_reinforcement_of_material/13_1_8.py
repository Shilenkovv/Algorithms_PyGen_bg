from typing import List


def rotate180(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n // 2):  # Переворачиваем строки по вертикали
        matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
    for i in range(n):  # Переворачиваем каждую строку
        matrix[i].reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotate180(matrix)
print(*matrix, sep='\n')
