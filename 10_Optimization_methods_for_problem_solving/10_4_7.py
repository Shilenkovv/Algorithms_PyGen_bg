def number_of_cinemas(times: list[tuple[int, int]]) -> int:
    start_times = sorted([start for start, end in times])
    end_times = sorted([end for start, end in times])

    i, j = 0, 0
    cur_films = 0
    max_films = 0

    while i < len(times):
        if start_times[i] < end_times[j]:
            cur_films += 1
            max_films = max(max_films, cur_films)
            i += 1
        else:
            cur_films -= 1
            j += 1

    return max_films


# print(number_of_cinemas([(0, 4), (5, 7), (10, 15), (16, 17)]))  # 1
# print(number_of_cinemas([(10, 20), (15, 16), (30, 32)]))  # 2
# print(number_of_cinemas([(1, 10), (2, 9), (3, 8), (4, 7)]))  # 4
# print(number_of_cinemas([(0, 5)]))  # 1
# print(number_of_cinemas([(1, 2), (1, 2), (1, 2)]))  # 3
# print(number_of_cinemas([(10, 12), (8, 10), (12, 14)]))  # 1
