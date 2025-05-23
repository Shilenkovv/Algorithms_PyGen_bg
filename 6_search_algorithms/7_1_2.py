def min_rectangle(points: list[tuple[int]]) -> list[tuple[int]]:
    min_x = min_y = float('inf')
    max_x = max_y = -float('inf')
    for x, y in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    return [(min_x, min_y), (max_x, max_y)]
