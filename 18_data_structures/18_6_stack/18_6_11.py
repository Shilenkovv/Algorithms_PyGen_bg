from typing import List


def max_correct(s: str) -> int:
    stack: List[int] = [-1]  # Начинаем со "сторожевого" индекса
    max_len = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            # char == ')', значит пытаемся закрыть
            if stack:
                stack.pop()

            if not stack:
                # Если стек пуст, положим текущий индекс как новую "базу"
                stack.append(i)
            else:
                # Длина правильной последовательности — разница между текущим индексом и вершиной стека
                max_len = max(max_len, i - stack[-1])

    return max_len


print(max_correct('()()(()(()())('))  # ()(()())
print(max_correct('())'))
