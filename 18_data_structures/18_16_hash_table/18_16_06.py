from collections import defaultdict


def first_unique(s: str) -> int:
    cntr: dict[str, int] = defaultdict(int)
    idx_dict: dict[str, int] = dict()

    for i in range(len(s)):
        cyl = s[i]
        cntr[cyl] += 1
        if cyl not in idx_dict:
            idx_dict[cyl] = i

    for k in cntr:
        if cntr[k] == 1:
            return idx_dict[k]
    return -1
