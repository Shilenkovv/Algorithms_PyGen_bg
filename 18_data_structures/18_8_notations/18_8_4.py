from typing import List


def simplify(exp: str) -> str:
    stack: List[str] = []
    exp_list = exp.split()

    for elem in exp_list:
        if elem.isalnum():
            stack.append(elem)
        else:
            b = stack.pop()
            a = stack.pop()
            if not a.isdigit() or not b.isdigit():
                stack.append(a)
                stack.append(b)
                stack.append(elem)
                continue
            else:
                a, b = int(a), int(b)
                match elem:
                    case '+':
                        stack.append(str(a + b))
                    case '-':
                        stack.append(str(a - b))
                    case '*':
                        stack.append(str(a * b))
                    case '/':
                        stack.append(str(int(a / b)))
                    case '^':
                        stack.append(str(a**b))
                    case _:
                        raise Exception(f'Unknown operand {elem}')
    return ' '.join(stack)


# print(simplify('2 4 + 5 x - *'))  # 6 5 x - *
# print(simplify('2 3 ^ 12 + y /'))  # 20 y /
print(simplify('2 5 * 8 4 / +'))  # 12
