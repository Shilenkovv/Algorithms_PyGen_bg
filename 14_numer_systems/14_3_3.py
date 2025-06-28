def find_number_system(str_num: str, num: int) -> int:
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
    for base in range(2, 37):
        ans = 0
        for i in range(n - 1, -1, -1):
            num_val = digits_dict.get(str_num[i])
            if num_val >= base:
                break
            ans += num_val * base ** (n - i - 1)
        if ans == num:
            return base


# print(find_number_system('1001', 9))  # 2
# print(find_number_system('102', 11))  # 3
# print(find_number_system('17', 32))  # 25
# print(find_number_system('25', 25))  # 10
# print(find_number_system('1E', 30))  # 16
