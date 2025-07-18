from typing import List


def make_good(s: str) -> str:
    stack: List[str] = []

    for i in range(len(s)):
        if (
            stack
            and stack[-1].lower() == s[i].lower()
            and (stack[-1].islower() and s[i].isupper() or stack[-1].isupper() and s[i].islower())
        ):
            stack.pop()
        else:
            stack.append(s[i])
    return ''.join(stack)


print(make_good('pytThon'))
