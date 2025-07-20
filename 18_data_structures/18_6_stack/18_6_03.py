from typing import List


def create_num(s: str) -> str:
    stack: List[int] = []
    res: List[str] = []
    for i in range(len(s) + 1):
        stack.append(i + 1)
        # разгружаем стек, если достигнут конец строки или следующий символ +
        if i == len(s) or (i < len(s) and s[i] == '+'):
            while stack:
                res.append(str(stack.pop()))
    return ''.join(res)


print(create_num('+-+'))
print(create_num('--'))
# print(is_correct('()'))  # True
# print(is_correct('(*)'))  # True
# print(is_correct('((*)'))  # True
# print(is_correct('*)()'))  # True
# print(is_correct('*(*(*)*)*'))
