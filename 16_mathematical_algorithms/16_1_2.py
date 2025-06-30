def is_divisible_by_nine(str_num: str) -> bool:
    tot_dig_sum = 0
    for dig in str_num:
        tot_dig_sum += int(dig)
    return not tot_dig_sum % 9


print(is_divisible_by_nine('135'))
print(is_divisible_by_nine('81'))
print(is_divisible_by_nine('82'))
