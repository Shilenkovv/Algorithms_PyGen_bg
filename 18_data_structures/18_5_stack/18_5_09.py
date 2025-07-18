from typing import List


def is_good(s: str) -> bool:
    stack: List[str] = []

    for elem in s:
        if elem != 'c':
            stack.append(elem)
        else:
            if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                for _ in range(2):
                    stack.pop()
            else:
                return False
    return not stack


print(is_good('aabcabcbc'))  # True
print(is_good('aabcabcc'))  # False
print(is_good('a'))  # False
print(is_good('abc'))  # True
print(is_good('abccba'))  # False
