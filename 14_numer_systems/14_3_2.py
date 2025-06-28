def to_decimal(str_num: str, base: int) -> int:
    digits_dict: dict[str, int] = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        'G': 16,
        'H': 17,
        'I': 18,
        'J': 19,
        'K': 20,
        'L': 21,
        'M': 22,
        'N': 23,
        'O': 24,
        'P': 25,
        'Q': 26,
        'R': 27,
        'S': 28,
        'T': 29,
        'U': 30,
        'V': 31,
        'W': 32,
        'X': 33,
        'Y': 34,
        'Z': 35,
    }

    n = len(str_num)
    ans = 0

    for i in range(n - 1, -1, -1):
        ans += digits_dict.get(str_num[i]) * base ** (n - i - 1)
    return ans


print(to_decimal('110101', 2))  # 53
print(to_decimal('314', 5))  # 84
print(to_decimal('E52F', 16))  # 58671
