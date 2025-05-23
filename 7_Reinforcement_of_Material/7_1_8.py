def binary_search(lines, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if lines[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def count_triangles(lines):
    n = len(lines)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            a = lines[i]
            b = lines[j]
            sum_ab = a + b
            k = binary_search(lines, j + 1, n - 1, sum_ab)
            count += k - j - 1

    return count


# # Тесты:
# print(count_triangles([2, 2, 5]))  # Вывод: 0
# print(count_triangles([3, 4, 5]))  # Вывод: 1
# print(count_triangles([5, 5, 5]))  # Вывод: 1
# print(count_triangles([1, 7, 7, 10]))  # Вывод: 2
# print(count_triangles([1, 2, 3, 4, 5]))  # Вывод: 3
# print(count_triangles([5, 6, 10, 11, 20, 21]))  # Вывод: 8
