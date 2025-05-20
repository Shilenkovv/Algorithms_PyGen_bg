def get_closest_element(nums, target):
    # Бинарный поиск
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Определение ближайшего элемента
    closest = nums[left]
    if left > 0:
        prev = nums[left - 1]
        # Выбор числа с учетом равенства разниц
        if abs(prev - target) < abs(closest - target) or (
            abs(prev - target) == abs(closest - target) and prev > closest
        ):
            closest = prev

    return closest
