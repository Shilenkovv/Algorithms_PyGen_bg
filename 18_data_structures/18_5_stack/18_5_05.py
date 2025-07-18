from typing import List


def is_correct(s: str) -> bool:
    par_dict = {')': '(', ']': '[', '}': '{'}
    stack: List[str] = []

    for elem in s:
        if elem not in par_dict:
            stack.append(elem)
        else:
            if not stack:
                return False
            elif stack[-1] == par_dict.get(elem):
                stack.pop()
            else:
                return False

    return not stack


print(is_correct('(){}[]'))  # True
print(is_correct('{()]'))  # Falase
print(is_correct('{}([])'))  # True
print(is_correct('{[]{'))  # False
