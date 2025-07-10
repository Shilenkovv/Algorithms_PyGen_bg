from math import gcd


def gcd_of_two_strings(s1: str, s2: str) -> str:
    # Проверяем условие равенства конкатенаций
    if s1 + s2 != s2 + s1:
        return ''

    # Находим НОД длин строк
    gcd_len = gcd(len(s1), len(s2))

    # Возвращаем подстроку длины gcd_len из s1
    return s1[:gcd_len]


# print(gcd_of_two_strings('abcabc', 'abc'))
# print(gcd_of_two_strings('bbbbb', 'bb'))
