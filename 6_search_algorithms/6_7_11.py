def special_list(nums: list[int]):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        count = len(nums) - mid - 1

        if nums[mid] >= count:
            right = mid
        else:
            left = mid + 1

    # Проверяем, что найденный индекс соответствует условию
    count = len(nums) - left
    return nums[left] >= count if left < len(nums) else False


# assert special_list([1, 3, 5])
# assert not special_list([1, 1, 1])
# assert not special_list([0, 1, 2, 2, 3])
