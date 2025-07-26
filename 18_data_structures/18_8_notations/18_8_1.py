from typing import List


def calculate(exp: str) -> int | float:
    stack: List[int | float] = []
    elems = exp.split()

    for elem in elems:
        if elem.isdigit():
            stack.append(int(elem))
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


# print(calculate('6 1 - 2 6 / * 2 7 + * 2 +'))  # 17

# print(calculate('2 4 + 5 3 - *'))  # 12

# print(calculate('2 3 ^ 12 + 5 /'))  # 4

# print(calculate('3 5 -'))  # -2
