def sort_by_prod_and_sum(lines: list[int, int]) -> None:
    lines.sort(key=lambda x: (x[0] * x[1], x[0] + x[1]))


# print(count_possible_squares([3, 4, 3, 5, 1, 3, 3]))
