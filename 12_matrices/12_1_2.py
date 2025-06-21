def is_symmetric(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i <= j:
                break
            else:
                if matrix[i][j] != matrix[j][i]:
                    return False
    return True


# matrix = [[-10, 1, 6], [1, 5, -3], [6, -3, 3]]

# print(is_symmetric(matrix))  # True

# matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

# print(is_symmetric(matrix))  # True

# matrix = [[1, 2], [3, 4]]

# print(is_symmetric(matrix))  # False
