def check_letters(s):
    lower_dict = {chr(i): False for i in range(97, 123)}
    upper_dict = {chr(i): False for i in range(65, 91)}
    for char in s:
        if char in lower_dict:
            lower_dict[char] = True
        elif char in upper_dict:
            upper_dict[char] = True
    ans = ''
    for lk, uk in zip(lower_dict, upper_dict):
        cur_tot = lower_dict.get(lk) + upper_dict.get(uk)
        ans += str(cur_tot // 2 + cur_tot % 2)
    return ans
