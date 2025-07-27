from collections import Counter
from typing import List


def pairs_with_sum(nums: List[int], k: int):
    count = Counter(nums)  # Счётчик элементов
    pairs = 0

    for x in list(count.keys()):
        y = k - x
        if x == y:
            # Если ищем пары из одинаковых чисел
            pairs += count[x] // 2
            count[x] = 0
        elif y in count and count[x] > 0 and count[y] > 0:
            # Количество пар — минимум из доступных элементов x и y
            pair_count = min(count[x], count[y])
            pairs += pair_count
            count[x] -= pair_count
            count[y] -= pair_count

    return pairs
