from typing import List


def next_greater(nums: List[int]) -> List[int | None]:
    stack: List[int] = []
    result: List[None | int] = []

    for elem in reversed(nums):
        while stack and stack[-1] <= elem:
            stack.pop()
        if not stack:
            result.append(None)
        else:
            result.append(stack[-1])
        stack.append(elem)

    return result[::-1]


print(next_greater([1, 3, 2, 4]))
