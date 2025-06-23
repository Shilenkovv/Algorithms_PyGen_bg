def find_point(lines: list[tuple[int, int]]) -> int:
    start_max = -float('inf')
    end_min = float('inf')

    for tpl in lines:
        start_max = max(start_max, tpl[0])
        end_min = min(end_min, tpl[1])
    return min(start_max, end_min) if end_min >= start_max else None


# print(find_point([(1, 2), (3, 4), (5, 6)]))
