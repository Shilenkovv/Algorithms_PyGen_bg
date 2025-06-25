from typing import List


def count_sublists_with_sum(nums: List[int], k: int) -> int:
    current_sum = 0
    prefix_sums = {0: 1}  # Инициализируем 0, чтобы учитывать подсписки, начинающиеся с начала
    count = 0

    for num in nums:
        current_sum += num
        # Проверяем, есть ли нужная префиксная сумма
        count += prefix_sums.get(current_sum - k, 0)
        # Обновляем словарь
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return count


# print(count_sublists_with_sum([1, 4, 6, 3, 1, 1], 5)) # 2
# print(count_sublists_with_sum([1, -2, 3, 4, -1, 0], 5))  # 3
# print(count_sublists_with_sum([5], 5))  # 1
