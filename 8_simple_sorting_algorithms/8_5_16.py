def length_of_painted_part(lines: list[tuple[int, int]]) -> int:
    lines.sort()
    left, right = lines[0]
    painted = right - left
    for current_left, current_right in lines:
        left = max(right, current_left)
        right = max(right, current_right)
        painted += right - left
    return painted
