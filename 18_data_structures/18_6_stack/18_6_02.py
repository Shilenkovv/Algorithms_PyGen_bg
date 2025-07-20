def is_correct(s: str) -> bool:
    low = 0
    high = 0
    for c in s:
        if c == '(':
            low += 1
            high += 1
        elif c == ')':
            low = max(low - 1, 0)
            high -= 1
        else:  # c == '*'
            low = max(low - 1, 0)
            high += 1
        if high < 0:
            return False
    return low == 0


# print(is_correct('()'))  # True
# print(is_correct('(*)'))  # True
# print(is_correct('((*)'))  # True
# print(is_correct('*)()'))  # True
# print(is_correct('*(*(*)*)*'))
