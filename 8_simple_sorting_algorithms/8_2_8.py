def sort_matrix(matrix: list[list[int]]) -> None:
    n = len(matrix)

    for i in range(n * n - 1):
        swapped = False
        for j in range(n * n - i - 1):
            if matrix[j // n][j % n] > matrix[(j + 1) // n][(j + 1) % n]:
                matrix[j // n][j % n], matrix[(j + 1) // n][(j + 1) % n] = (
                    matrix[(j + 1) // n][(j + 1) % n],
                    matrix[j // n][j % n],
                )
                swapped = True
        if not swapped:
            break


# matrix = [[4, 5, 3], [1, 7, 8], [9, 2, 6]]

# sort_matrix(matrix)
# print(*matrix, sep='\n')
