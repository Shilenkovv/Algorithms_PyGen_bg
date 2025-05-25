def closest_point(radius: int, points: list[tuple[int, int]]) -> tuple[int, int]:
    min_dist = float('inf')
    coords = (float('inf'), float('inf'))
    for tpl in points:
        cur_dist_from_circle = (tpl[0] ** 2 + tpl[1] ** 2) ** 0.5 - radius
        if cur_dist_from_circle > 0:
            if cur_dist_from_circle < min_dist:
                min_dist = cur_dist_from_circle
                coords = tpl
            elif cur_dist_from_circle == min_dist and (
                tpl[0] < coords[0] or (tpl[0] == coords[0] and tpl[1] < coords[1])
            ):
                coords = tpl
    return coords if coords[0] != float('inf') else None


# print(closest_point(5, [(7, 3), (6, 1), (3, 4)]))
# print(closest_point(5, [(0, 6), (0, -6), (-6, 0), (6, 0)]))
