# from typing import List


def has_double_brackets(exp: str) -> bool:
    # par_dict = {')': '(', ']': '[', '}': '{'}
    # stack: List[str] = []
    cur_len = len(exp)
    i = 0
    cnt = 0
    while i < cur_len and cnt < 2:
        if exp[i] == '(':
            cnt += 1
        elif exp[i] == ')':
            cnt -= 1
        i += 1
    return cnt == 2


# print(has_double_brackets('((1+2))'))  # True
# print(has_double_brackets('(1+2)*3'))  # False
# print(has_double_brackets('((1+2)*(3+4))'))  # True
