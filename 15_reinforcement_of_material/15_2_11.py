def filter_and_sort_even_numbers(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        if num % 2 == 0:
            oct_str = format(num, 'o')  # восьмеричное представление без '0o'
            # третья справа цифра — индекс -3
            third_digit = int(oct_str[-3])
            if third_digit % 2 == 1:  # проверяем нечетность
                result.append(num)
    return sorted(result)
