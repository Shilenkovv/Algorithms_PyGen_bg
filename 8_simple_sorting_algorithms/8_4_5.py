def sort_limited_numbers(nums: list[int]) -> None:
    counts = [0] * 201
    min_value = -100

    for num in nums:
        counts[num - min_value] += 1

    index = 0

    # Восстанавливаем массив в порядке убывания
    for num in range(100, -101, -1):
        for _ in range(counts[num - min_value]):
            nums[index] = num
            index += 1


# nums = [-15, 10, 1, -8, 24]  # [24, 10, 1, -8, -15]
# sort_limited_numbers(nums)
# print(nums)
