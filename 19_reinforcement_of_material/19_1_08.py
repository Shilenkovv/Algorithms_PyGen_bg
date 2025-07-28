def can_transform(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    if s1 == s2:
        # Нужно проверить, есть ли повторяющиеся символы для допустимого обмена
        seen = set()
        for ch in s1:
            if ch in seen:
                return True
            seen.add(ch)
        return False

    diff_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]
    if len(diff_indices) != 2:
        return False

    i, j = diff_indices
    return s1[i] == s2[j] and s1[j] == s2[i]


# print(can_transform('ab', 'abc'))
# print(can_transform('abca', 'abca'))
print(can_transform('abab', 'abba'))
print(can_transform('abcd', 'wxyz'))
