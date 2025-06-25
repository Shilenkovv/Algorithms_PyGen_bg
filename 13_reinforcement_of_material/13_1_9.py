from typing import List


def create_matrix(n: int, m: int) -> List[List[int]]:
    # Create an empty matrix with zeros
    matrix = [[0] * m for _ in range(n)]

    # Determine the number of layers
    layers = (min(n, m) + 1) // 2

    for layer in range(layers):
        # Fill top and bottom rows of the current layer
        for j in range(layer, m - layer):
            matrix[layer][j] = layer + 1
            matrix[n - layer - 1][j] = layer + 1

        # Fill left and right columns of the current layer
        for i in range(layer + 1, n - layer - 1):
            matrix[i][layer] = layer + 1
            matrix[i][m - layer - 1] = layer + 1

    return matrix


# matrix = create_matrix(5, 1)
# print(*matrix, sep='\n')

# # [1]
# # [1]
# # [1]
# # [1]
# # [1]

# matrix = create_matrix(6, 7)
# print(*matrix, sep='\n')

# # [1, 1, 1, 1, 1, 1, 1]
# # [1, 2, 2, 2, 2, 2, 1]
# # [1, 2, 3, 3, 3, 2, 1]
# # [1, 2, 3, 3, 3, 2, 1]
# # [1, 2, 2, 2, 2, 2, 1]
# # [1, 1, 1, 1, 1, 1, 1]

# matrix = create_matrix(3, 3)
# print(*matrix, sep='\n')

# # [1, 1, 1]
# # [1, 2, 1]
# # [1, 1, 1]

# matrix = create_matrix(2, 5)
# print(*matrix, sep='\n')

# # [1, 1, 1, 1, 1]
# # [1, 1, 1, 1, 1]

# matrix = create_matrix(3, 5)
# print(matrix)

# # [[1, 1, 1, 1, 1],
# #  [1, 2, 2, 2, 1],
# #  [1, 1, 1, 1, 1]]
