from typing import List


def to_postfix(exp: str) -> str:
    stack: List[str] = []
    exp_list = exp.split()
    ans: List[str] = []

    for elem in exp_list:
        if elem.isdigit():
            ans.append(elem)
        elif elem == '(':
            stack.append(elem)
        elif elem == ')':
            while stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        elif elem == '+' or elem == '-':
            while stack and not stack[-1].isdigit() and stack[-1] != '(':
                ans.append(stack.pop())
            stack.append(elem)
        elif elem == '*' or elem == '/':
            while stack and stack[-1] not in ['+', '-'] and stack[-1] != '(':
                ans.append(stack.pop())
            stack.append(elem)
        elif elem == '^':
            while stack and stack[-1] not in ['+', '-', '*', '/'] and stack[-1] != '(':
                ans.append(stack.pop())
            stack.append(elem)
    while stack:
        ans.append(stack.pop())
    return ' '.join(ans)


# print(to_postfix('( ( 2 + 3 ) * 4 ) / 10'))  # 2 3 + 4 * 10 /
