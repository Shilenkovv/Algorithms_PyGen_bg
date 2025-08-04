from typing import List, Tuple


def max_viewers(sessions: List[Tuple[int, int, int]]) -> int:
    events: List[Tuple[int, int, int]] = []
    for start, end, viewers in sessions:
        events.append((start, 1, viewers))  # начало сессии
        events.append((end, 0, viewers))  # конец сессии

    # Сортируем: по времени, затем по типу (0 - конец, 1 - начало)
    events.sort(key=lambda x: (x[0], x[1]))

    cur_viewers = 0
    max_viewers = 0
    for _, typ, v in events:
        if typ == 0:
            cur_viewers -= v
        else:
            cur_viewers += v
            if cur_viewers > max_viewers:
                max_viewers = cur_viewers

    return max_viewers


# print(max_viewers([(1, 4, 3), (2, 5, 4), (7, 9, 6)]))  # 7
# print(max_viewers([(6, 7, 10), (2, 4, 11), (8, 12, 15)]))  # 15
# print(max_viewers([(1, 2, 1), (2, 3, 2), (3, 4, 3)]))  # 3
