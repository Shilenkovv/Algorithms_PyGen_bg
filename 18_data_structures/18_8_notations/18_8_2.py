from typing import List


def calculate(exp: str) -> int | float:
    stack: List[int | float] = []
    elems = exp.split()

    for elem in elems:
        if elem.isdigit():
            stack.append(int(elem))
        elif elem == 'NEGATE':
            stack.append(-1 * stack.pop())
        else:
            b = stack.pop()
            a = stack.pop()
            match elem:
                case '+':
                    stack.append(a + b)
                case '-':
                    stack.append(a - b)
                case '*':
                    stack.append(a * b)
                case '/':
                    stack.append(a / b)
                case '^':
                    stack.append(a**b)
                case _:
                    raise Exception(f'Unknown operand {elem}')
    return stack[0]


# print(calculate('2 4 + 5 3 - *')) # 12

print(calculate('3 NEGATE'))
