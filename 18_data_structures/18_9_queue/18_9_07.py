from collections import deque


def smallest_num(n: int) -> int:
    if n == 1:
        return 9
    queue = deque()
    queue.append('9')
    visited = set()
    while queue:
        num_str = queue.popleft()
        remainder = int(num_str) % n
        if remainder == 0:
            return int(num_str)
        # Помечаем остаток, чтобы не идти по кругу
        if remainder not in visited:
            visited.add(remainder)
            queue.append(num_str + '0')
            queue.append(num_str + '9')
