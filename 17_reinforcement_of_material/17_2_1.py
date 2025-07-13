def is_divisible_by_twelve(str_num: str) -> bool:
    last_2_dig = int(str_num[-2:])
    if last_2_dig % 4:
        return False
    dig_sum = 0
    for i in range(len(str_num)):
        dig_sum += int(str_num[i])
    if dig_sum % 3:
        return False
    return True
