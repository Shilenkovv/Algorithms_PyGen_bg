from typing import List


def missing_member(nums: List[int]) -> int:
    if len(nums) == 2:
        return (nums[-1] + nums[0]) // 2
    elif nums[0] == nums[-1]:
        return nums[0]
    n = len(nums) + 1
    d = (nums[-1] - nums[0]) // (n - 1)

    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2
        cur_n = mid - left + 1
        sum_should_be = ((2 * nums[left] + d * (cur_n - 1)) * cur_n) // 2
        cur_sum = ((nums[left] + nums[mid]) * cur_n) // 2

        if cur_sum == sum_should_be:
            if nums[mid] + d != nums[mid + 1]:
                return nums[mid] + d
            left = mid + 1
        else:
            if nums[mid] - d != nums[mid - 1]:
                return nums[mid] - d
            right = mid - 1

    if nums[left] - d == nums[left - 1]:
        return nums[left] + d
    return nums[left] - d


# print(missing_member([1, 2, 4, 5, 6, 7, 8]))  # 3
# print(missing_member([2, 4, 6, 10, 12, 14]))  # 8
# print(missing_member([2, 4]))  # 3
# print(missing_member([-5, -4, -3, -1, 0]))  # -2
