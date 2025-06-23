def sum_of_five_largest_and_smallest(nums: list[int]) -> tuple[int, int]:
    n = len(nums)
    start = 0
    end = n - 1
    largest_sum = smallest_sum = 0

    for _ in range(5):
        for i in range(start, end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        largest_sum += nums[end]
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        smallest_sum += nums[start]
        start += 1

    return largest_sum, smallest_sum
