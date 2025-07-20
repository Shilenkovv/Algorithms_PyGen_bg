from collections import defaultdict


def remove_brackets(s: str) -> int:
    par_dict = {')': '(', ']': '[', '}': '{'}
    counter_dict = defaultdict(int)
    cur_len = len(s)

    for elem in s:
        if elem not in par_dict:
            counter_dict[elem] += 1
        else:
            if par_dict[elem] in counter_dict and counter_dict[par_dict[elem]] > 0:
                counter_dict[par_dict[elem]] -= 1
                cur_len -= 2
    return cur_len


# print(remove_brackets('(])(['))
