def max_value(strings: list[str]) -> int:
    cur_max_value = -float('inf')
    for s in strings:
        if s.isnumeric():
            cur_max_value = max(cur_max_value, int(s))
        else:
            cur_max_value = max(cur_max_value, len(s))
    return cur_max_value
