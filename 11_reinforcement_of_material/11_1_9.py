def max_water_container(lines: list[int]) -> int:
    left, right = 0, len(lines) - 1
    max_volume = 0

    while left < right:
        # Высота контейнера определяется меньшей из двух линий
        height = min(lines[left], lines[right])
        # Ширина контейнера — это расстояние между указателями
        width = right - left
        # Вычисляем объем контейнера
        volume = height * width
        # Обновляем максимальный объем
        max_volume = max(max_volume, volume)

        # Двигаем указатель с меньшей линией
        if lines[left] < lines[right]:
            left += 1
        else:
            right -= 1

    return max_volume


print(max_water_container([3, 6, 5, 1, 4, 7, 5, 2, 4]))  # 2 и 9 линии # 28
