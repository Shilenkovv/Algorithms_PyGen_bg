from collections import deque


def remove_substrings(s: str) -> int:
    deq: deque[str] = deque()

    for elem in s:
        if not deq:
            deq.append(elem)
        else:
            if elem == 'B' and deq[-1] == 'A':
                deq.pop()
            elif elem == 'D' and deq[-1] == 'C':
                deq.pop()
            else:
                deq.append(elem)
    return len(deq)


# print(remove_substrings('RCABD'))  # 1
# print(remove_substrings('ABACD'))  # 1
# print(remove_substrings('AAABBB'))  # 0
