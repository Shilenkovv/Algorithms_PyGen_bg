from typing import List


def min_add_to_balance(s: str) -> int:
    # par_dict = {')': '(', ']': '[', '}': '{'}
    stack: List[str] = []
    cnt = 0

    for elem in s:
        if elem == '(':
            stack.append(elem)
        elif elem == ')':
            if not stack:
                cnt += 1
            elif stack[-1] != '(':
                cnt += 1
            else:
                stack.pop()
    cnt += len(stack)
    return cnt


print(min_add_to_balance('())'))  # 1
print(min_add_to_balance(')))'))  # 3
print(min_add_to_balance('()()()'))  # 0
print(min_add_to_balance(')))((('))  # 6
print(min_add_to_balance('(()('))  # 2
