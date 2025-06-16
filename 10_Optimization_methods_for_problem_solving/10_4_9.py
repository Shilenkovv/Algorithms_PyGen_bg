def len_of_shortest_unsorted_part(nums: list[int]):
    n = len(nums)
    start, end = 0, -1
    max_seen, min_seen = float('-inf'), float('inf')

    # Найти конец "неправильного" сегмента
    for i in range(n):
        max_seen = max(max_seen, nums[i])
        if nums[i] < max_seen:
            end = i

    # Найти начало "неправильного" сегмента
    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, nums[i])
        if nums[i] > min_seen:
            start = i

    return end - start + 1 if end != -1 else 0


# # Тестовые примеры
# print(len_of_shortest_unsorted_part([1, 2, 4, 3, 6, 5, 7]))  # 4
# print(len_of_shortest_unsorted_part([7, 6, 5, 4, 3, 2, 1]))  # 7
# print(len_of_shortest_unsorted_part([1, 2, 3, 4, 5, 6, 7]))  # 0
# print(len_of_shortest_unsorted_part([-3, -4, -1, 0, 1, 2]))  # 2
# print(len_of_shortest_unsorted_part([-4, 10, 15, 20, 0]))  # 4
# print(len_of_shortest_unsorted_part([-8, -7, -2, -4, -1]))  # 2


# print(len_of_shortest_unsorted_part([1, 2, 4, 3, 6, 5, 7]))  # [4, 3, 6, 5] # 4
# print(len_of_shortest_unsorted_part([7, 6, 5, 4, 3, 2, 1]))  # 7
# print(len_of_shortest_unsorted_part([1, 2, 3, 4, 5, 6, 7]))  # 0
