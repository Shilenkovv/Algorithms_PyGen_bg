from typing import List, Tuple


def increase_numbers_on_segments(nums: List[int], segments: List[Tuple[int, int]], k: int) -> None:
    n = len(nums)
    delta = [0] * (n + 1)  # Вспомогательный массив для учета изменений

    # Обновляем вспомогательный массив на основе сегментов
    for start, end in segments:
        delta[start] += k
        if end + 1 < n:
            delta[end + 1] -= k

    # Применяем изменения к nums с помощью префиксных сумм
    current_addition = 0
    for i in range(n):
        current_addition += delta[i]
        nums[i] += current_addition


# # Примеры использования
# nums = [3, 1, 4, 5, 2]
# increase_numbers_on_segments(nums, [(0, 4), (0, 1), (3, 4)], 1)
# print(nums)  # [5, 3, 5, 7, 4]

# nums = [-1, 0, 2, -4, 3]
# increase_numbers_on_segments(nums, [(0, 4), (0, 1), (3, 4)], 5)
# print(nums)  # [9, 10, 7, 6, 13]

# nums = [2, 6, 1, 3, 1, 5]
# increase_numbers_on_segments(nums, [(0, 4), (0, 1), (3, 4)], 0)
# print(nums)  # [2, 6, 1, 3, 1, 5]

# nums = [0, 0, 0, 0, 0]
# increase_numbers_on_segments(nums, [(0, 4), (0, 3), (0, 2), (0, 1), (0, 0)], 1)
# print(nums)  # [5, 4, 3, 2, 1]

# nums = [1]
# increase_numbers_on_segments(nums, [(0, 0)], 1)
# print(nums)  # [2]

# nums = [1, 2, 3, 4, 5]
# increase_numbers_on_segments(nums, [(4, 4), (3, 4), (2, 4), (1, 4)], -1)
# print(nums)  # [1, 1, 1, 1, 1]
