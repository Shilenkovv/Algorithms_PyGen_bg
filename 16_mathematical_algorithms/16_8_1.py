from typing import List


def generate_arithmetic(start: int, step: int, n: int) -> List[int]:
    return [start + step * i for i in range(n)]


print(generate_arithmetic(1, 1, 3))
print(generate_arithmetic(0, 2, 5))
