def is_divisible_by_forty(str_num: str) -> bool:
    if str_num[-1] == '5' or str_num[-1] == '0':
        if len(str_num) >= 3:
            if not int(str_num[-3:]) % 8:
                return True
        elif not int(str_num) % 8:
            return True
    return False


# print(is_divisible_by_forty('40'))  # True
# print(is_divisible_by_forty('55'))  # False
# print(is_divisible_by_forty('0'))  # True
