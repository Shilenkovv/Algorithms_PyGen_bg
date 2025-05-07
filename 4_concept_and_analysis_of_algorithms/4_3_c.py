def parse_max(s: str) -> int:
    max_num = -1
    cur_num = ''
    s += ' '

    for sym in s:
        if sym.isdigit():
            cur_num += sym
        elif cur_num:
            max_num = max(max_num, int(cur_num))
            cur_num = ''

    return max_num
