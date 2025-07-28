def steps_to_transform(s1: str, s2: str) -> int | None:
    if len(s1) != len(s2):
        return None

    # Проверка, что строки являются перестановками друг друга
    from collections import Counter

    if Counter(s1) != Counter(s2):
        return None

    i = len(s1) - 1
    j = len(s2) - 1

    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:
            i -= 1
            j -= 1
        else:
            i -= 1

    # j + 1 — кол-во символов в s2, для которых не найдено соответствия в s1 при движении с конца
    return j + 1
