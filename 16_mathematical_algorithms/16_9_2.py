from typing import List


def generate_geometric(start: int | float, ratio: int | float, n: int) -> List[int | float]:
    ans: List[float, int] = []
    for i in range(1, n + 1):
        ans.append(start * ratio ** (i - 1))
    return ans


print(generate_geometric(1, 2, 5))
