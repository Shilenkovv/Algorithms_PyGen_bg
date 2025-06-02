def remove_covered_segments(segments: list[tuple[int, int]]) -> int:
    segments.sort(key=lambda x: (x[0], -x[1]))

    remaining = 0
    prev_end = float('-inf')

    for _, end in segments:
        if end > prev_end:
            remaining += 1
            prev_end = end

    return remaining


# print(remove_covered_segments([(2, 5), (1, 7), (5, 9)]))
