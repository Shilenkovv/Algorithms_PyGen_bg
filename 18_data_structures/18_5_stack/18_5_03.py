from typing import List


def remove_digits(s: str) -> str:
    stack: List[str] = []

    for i in range(len(s)):
        if s[i].isalpha():
            stack.append(s[i])
        elif stack and s[i].isdigit():
            stack.pop()
    return ''.join(stack)


print(remove_digits('abc12'))  # a
print(remove_digits('12abc'))  # abc
