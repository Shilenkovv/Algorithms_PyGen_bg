def roman_to_arabic(roman_num: str) -> int:
    roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    idx = 0
    n = len(roman_num)
    ans = 0

    while idx < n - 1:
        first_dig = roman_to_arabic[roman_num[idx]]
        second_dig = roman_to_arabic[roman_num[idx + 1]]

        if first_dig < second_dig:
            ans += second_dig - first_dig
            idx += 2
        else:
            ans += first_dig
            idx += 1
    if idx == n - 1:
        ans += roman_to_arabic[roman_num[idx]]
    return ans


print(roman_to_arabic('XIX'))  # 19
print(roman_to_arabic('XVIII'))  # 18
print(roman_to_arabic('LXII'))  # 62
