from collections import deque
from typing import List, Tuple


def erase_order(write_down: List[Tuple[int, str]], write_out: List[str]) -> List[int]:
    deq: deque[int] = deque()
    ans: List[int] = []

    for num, order in write_down:
        if order == 'left':
            deq.appendleft(num)
        else:
            deq.append(num)

    for out_order in write_out:
        if out_order == 'left':
            ans.append(deq.popleft())
        else:
            ans.append(deq.pop())

    return ans


write_down = [(2, 'left'), (4, 'right'), (6, 'left'), (8, 'right')]
write_out = ['left', 'right', 'right', 'left']
print(erase_order(write_down, write_out))  # [6, 8, 4, 2]

write_down = [(-3, 'right'), (-2, 'left'), (6, 'left'), (3, 'left')]
write_out = ['left', 'right', 'right', 'left']
print(erase_order(write_down, write_out))  # [3, -3, -2, 6]
