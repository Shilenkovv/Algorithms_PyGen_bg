from typing import List


def can_rearrange(train_cars: List[int]) -> bool:
    stack: List[int | float] = []
    n = len(train_cars)

    i = 0
    looking_for = 1

    while i <= n and looking_for <= n:
        while stack and stack[-1] == looking_for:
            stack.pop()
            looking_for += 1
        if i < n:
            stack.append(train_cars[i])
        i += 1

    return not stack and looking_for > n


print(can_rearrange([3, 2, 1]))  # True
print(can_rearrange([4, 1, 3, 2]))  # True
print(can_rearrange([2, 3, 1]))  # False
