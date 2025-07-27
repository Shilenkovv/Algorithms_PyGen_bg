from typing import List


def longest_sublist(nums: List[int]) -> int:
    nums_set = set(nums)
    max_len = 0

    for num in nums_set:
        # Проверяем, что это начало последовательности
        if num - 1 not in nums_set:
            length = 1
            current = num

            # Пробуем идти по последовательности вверх
            while current + 1 in nums_set:
                current += 1
                length += 1

            max_len = max(max_len, length)

    return max_len
