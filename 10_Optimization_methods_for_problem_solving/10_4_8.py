def count_triplets_with_lower_sum(nums: list[int], value: int) -> int:
    # Сортируем список для удобства использования двух указателей
    nums.sort()
    n = len(nums)
    count = 0

    # Фиксируем первый элемент тройки
    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            # Сумма текущей тройки
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum < value:
                # Если сумма меньше, то все пары между left и right подходят
                count += right - left
                left += 1
            else:
                # Иначе уменьшаем правый указатель
                right -= 1

    return count


# print(count_triplets_with_lower_sum([2, 4, -2, 3], 6))  # (2, 4, -2), (2, -2, 3), (4, -2, 3) # 3
