def create_matrix(n: int, m: int) -> list[list[int]]:
    matrix = [[0] * m for _ in range(n)]

    number = 1
    for diag in range(n + m - 1):
        if diag % 2 == 0:  # Fill diagonals from top-right to bottom-left
            row = max(0, diag - m + 1)
            col = min(diag, m - 1)
        else:  # Fill diagonals from bottom-left to top-right
            col = max(0, diag - n + 1)
            row = min(diag, n - 1)

        while 0 <= row < n and 0 <= col < m:
            matrix[row][col] = number
            number += 1
            if diag % 2 == 0:
                row += 1
                col -= 1
            else:
                row -= 1
                col += 1

    return matrix


# Example usage
matrix = create_matrix(4, 5)
print(*matrix, sep='\n')
