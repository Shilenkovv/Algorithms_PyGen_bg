def count_possible_squares(lines: list[int, int]) -> int:
    counts = [0] * 100

    for elem in lines:
        counts[elem - 1] += 1

    tot_squares = 0
    for i in range(100):
        tot_squares += counts[i] // 4

    return tot_squares


# print(count_possible_squares([3, 4, 3, 5, 1, 3, 3]))
