def rotate90(matrix: list[list[int]]) -> None:
    n = len(matrix)
    # Транспонируем матрицу
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Зеркально отражаем строки
    for i in range(n):
        matrix[i].reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotate90(matrix)
print(*matrix, sep='\n')
