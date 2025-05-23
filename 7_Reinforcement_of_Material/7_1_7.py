def lower_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def upper_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def count_triplets(nums1, nums2, nums3):
    count = 0
    n = len(nums2)

    for num in nums2:
        left_count = lower_bound(nums1, num)
        right_count = n - upper_bound(nums3, num)
        count += left_count * right_count

    return count


# Тесты:
# print(count_triplets([1, 5], [2, 4], [3, 6]))  # Вывод: 3
# print(count_triplets([1], [2], [3]))           # Вывод: 1
# print(count_triplets([1, 1, 1], [2, 2, 2], [3, 3, 3]))  # Вывод: 27
# print(count_triplets([1, 1, 1], [0, 0, 0], [-1, -1, -1]))  # Вывод: 0
# print(count_triplets([1, 1, 1], [1, 1, 1], [1, 1, 1]))  # Вывод: 0
# print(count_triplets([-2, -1], [0, 1], [2, 3]))  # Вывод: 6
