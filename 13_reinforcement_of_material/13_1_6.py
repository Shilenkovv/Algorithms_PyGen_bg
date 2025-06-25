def create_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    elem = 0

    for start in range(n):
        i, j = 0, start

        while i < n and j < n:
            if not elem % 3:
                break
            matrix[i][j] = elem % 3
            i += 1
            j += 1
        elem += 1

    elem = 2
    for start in range(1, n):
        i, j = start, 0

        while i < n and j < n:
            if not elem % 3:
                break
            matrix[i][j] = elem % 3
            i += 1
            j += 1
        elem -= 1
    return matrix


# matrix = create_matrix(5)
# print(*matrix, sep='\n')
# # Sample Output 1:

# # [0, 1, 2, 0, 1]
# # [2, 0, 1, 2, 0]
# # [1, 2, 0, 1, 2]
# # [0, 1, 2, 0, 1]
# # [2, 0, 1, 2, 0]

# matrix = create_matrix(3)
# print(*matrix, sep='\n')

# # [0, 1, 2]
# # [2, 0, 1]
# # [1, 2, 0]
