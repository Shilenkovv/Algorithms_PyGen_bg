def create_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]

    number = 1
    top, left = 0, 0
    bottom, right = n - 1, m - 1

    while top <= bottom and left <= right:
        # Fill top row
        for col in range(left, right + 1):
            matrix[top][col] = number
            number += 1
        top += 1

        # Fill right column
        for row in range(top, bottom + 1):
            matrix[row][right] = number
            number += 1
        right -= 1

        if top <= bottom:
            # Fill bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = number
                number += 1
            bottom -= 1

        if left <= right:
            # Fill left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = number
                number += 1
            left += 1

    return matrix


# Example usage
matrix = create_matrix(3, 4)
print(*matrix, sep='\n')
