from typing import List


def validate(pushed: List[int], popped: List[int]) -> bool:
    stack: List[int] = []
    pop_i = 0  # Индекс текущего элемента в popped

    for num in pushed:
        stack.append(num)  # push элемент
        # Проверяем, можем ли popить из стека, чтобы совпало с элементом из popped
        while stack and pop_i < len(popped) and stack[-1] == popped[pop_i]:
            stack.pop()
            pop_i += 1

    # Если после обработки всего pushed стек пуст, значит валидно
    return not stack


print(validate([1, 2, 3, 4], [3, 4, 2, 1]))  # True
print(validate([1, 2, 3, 4], [3, 4, 1, 2]))  # False
