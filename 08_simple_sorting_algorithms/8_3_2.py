def binary_insertion_sort(nums: list[int]) -> None:
    n = len(nums)

    for i in range(1, n):
        item = nums[i]
        left = 0
        right = i - 1

        while left <= right:
            mid = (left + right) // 2
            if item < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        for j in range(i, left, -1):
            nums[j] = nums[j - 1]

        nums[left] = item


# nums = [3, 4, 1, 2, 5]
# insertion_sort(nums)
# print(nums)
