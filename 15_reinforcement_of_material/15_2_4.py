from string import ascii_uppercase


def column_number(title: str) -> int:
    LETTERS = ascii_uppercase
    ans = 0
    n = len(title)
    for i in range(n - 1, -1, -1):
        ans += (LETTERS.index(title[i]) + 1) * 26 ** (n - 1 - i)

    return ans


# print(column_number('A'))  # 1
# print(column_number('AA'))  # 27
# print(column_number('BA'))  # 53
# print(column_number('AAA'))  # 703
# print(column_number('BEEGEEK'))  # 679649865
