def is_toeplitz_matrix(matrix: list[list[int]]) -> True:
    n = len(matrix)

    for start in range(n):
        i, j = 0, start
        elem = set()
        while i < n and j < n:
            elem.add(matrix[i][j])
            if len(elem) != 1:
                return False
            i += 1
            j += 1

    for start in range(1, n):
        i, j = start, 0
        elem = set()
        while i < n and j < n:
            elem.add(matrix[i][j])
            if len(elem) != 1:
                return False
            i += 1
            j += 1
    return True


# matrix = [[0, 1, 3, 4], [2, 0, 1, 3], [4, 2, 0, 1], [3, 4, 2, 0]]

# print(is_toeplitz_matrix(matrix))  # True


# matrix = [[1, 5, 7], [4, 2, 5], [6, 4, 3]]

# print(is_toeplitz_matrix(matrix))  # False

# matrix = [[1]]

# print(is_toeplitz_matrix(matrix))  # True

# matrix = [[10, 0], [0, 10]]

# print(is_toeplitz_matrix(matrix))  # True
