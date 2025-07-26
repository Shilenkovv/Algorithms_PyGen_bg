from typing import List


def to_postfix(exp: str) -> str:
    # Приоритеты операторов: выше число = выше приоритет
    # Унарный минус (NEGATE) имеет максимальный приоритет и правую ассоциативность
    preced = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'NEGATE': 4}
    # Ассоциативность: True = левый, False = правый
    left_assoc = {'+': True, '-': True, '*': True, '/': True, '^': False, 'NEGATE': False}

    stack: List[str] = []
    tokens = exp.split()
    ans: List[str] = []

    # Нужно отличать унарный минус от бинарного:
    # унарный, если текущий '-' и предыдущий токен:
    # None (начало), '(' или оператор
    prev_token = None

    for token in tokens:
        if token.isdigit():
            ans.append(token)
            prev_token = 'operand'
        elif token == '(':
            stack.append(token)
            prev_token = '('
        elif token == ')':
            # Все операторы из стека до '(' попадают в ans
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()  # убираем '('
            prev_token = ')'
        elif token == '-':
            # Проверяем унарный или бинарный минус
            if prev_token in (
                None,
                'operator',
                '(',
            ):
                # унарный минус
                op = 'NEGATE'
            else:
                op = '-'

            # Обработка стека по приоритетам (стандартный алгоритм для операторов)
            while stack and stack[-1] != '(':
                top = stack[-1]
                if (left_assoc[op] and preced[op] <= preced[top]) or (
                    not left_assoc[op] and preced[op] < preced[top]
                ):
                    ans.append(stack.pop())
                else:
                    break
            stack.append(op)
            prev_token = 'operator'
        elif token in ('+', '*', '/', '^'):
            op = token
            while stack and stack[-1] != '(':
                top = stack[-1]
                if (left_assoc[op] and preced[op] <= preced[top]) or (
                    not left_assoc[op] and preced[op] < preced[top]
                ):
                    ans.append(stack.pop())
                else:
                    break
            stack.append(op)
            prev_token = 'operator'
        else:
            # В условии допустимые токены: цифры, скобки, операторы
            # Если встретили что-то неожиданное — можем бросить ошибку или пропустить
            raise ValueError(f'Unexpected token: {token}')

    # В конце вынимаем все оператор из стека
    while stack:
        ans.append(stack.pop())

    return ' '.join(ans)
