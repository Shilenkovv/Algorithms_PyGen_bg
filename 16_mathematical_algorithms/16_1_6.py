from collections import defaultdict
from typing import List


def create_number(digits: List[int]):
    # Проверка наличия 0
    if 0 not in digits:
        return -1

    digits.sort(reverse=True)
    total_sum = sum(digits)

    # Группируем цифры по остатку от деления на 3
    remainder_buckets = defaultdict(list)
    for d in digits:
        remainder_buckets[d % 3].append(d)

    remainder = total_sum % 3

    def remove_digits(rem):
        # Удаляем минимальное количество цифр, чтобы сумма делилась на 3
        if rem == 0:
            return True
        elif rem == 1:
            # Сначала пытаемся удалить одну цифру с остатком 1
            if remainder_buckets[1]:
                remainder_buckets[1].pop()
                return True
            # Иначе удаляем две цифры с остатком 2
            elif len(remainder_buckets[2]) >= 2:
                remainder_buckets[2].pop()
                remainder_buckets[2].pop()
                return True
            else:
                return False
        elif rem == 2:
            # Сначала пытаемся удалить одну цифру с остатком 2
            if remainder_buckets[2]:
                remainder_buckets[2].pop()
                return True
            # Иначе удаляем две цифры с остатком 1
            elif len(remainder_buckets[1]) >= 2:
                remainder_buckets[1].pop()
                remainder_buckets[1].pop()
                return True
            else:
                return False

    if not remove_digits(remainder):
        return -1

    # Собираем все оставшиеся цифры из buckets
    result_digits = remainder_buckets[0] + remainder_buckets[1] + remainder_buckets[2]
    if not result_digits:
        return -1

    result_digits.sort(reverse=True)

    # Если все цифры — нули, вернуть 0
    if all(d == 0 for d in result_digits):
        return 0

    # Проверяем, что есть хотя бы один 0 для делимости на 10
    if 0 not in result_digits:
        return -1

    # Формируем число из цифр
    return int(''.join(map(str, result_digits)))


# print(create_number([0, 3, 4, 5, 3]))  # 54330
# print(create_number([5, 4, 5, 2, 1]))  # -1
# print(create_number([1]))  # -1
# print(create_number([0]))  # 0
