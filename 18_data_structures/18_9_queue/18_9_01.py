from collections import Counter


def eval_queue(s: str) -> str:
    n_stars = Counter(s).get('*', 0)
    s = s.replace('*', '')
    return ' '.join(list(s[n_stars:]))


print(eval_queue('ab*cd*'))
