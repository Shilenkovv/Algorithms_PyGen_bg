from typing import List


def remove_duplicates(s: str) -> str:
    stack: List[str] = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return ''.join(stack)


print(remove_duplicates('abccbd'))  # ad
print(remove_duplicates('abcd'))  # abcd
print(remove_duplicates('xyyxzx'))  # zx
