def count_rescue_attempts(weights: list[int], limit: int) -> int:
    weights.sort()

    left = 0
    right = len(weights) - 1
    attempts = 0

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        attempts += 1

    return attempts


# print(count_rescue_attempts([1, 2], 3))  # Output: 1
# print(count_rescue_attempts([2, 3, 2, 1], 4))  # Output: 2
# print(count_rescue_attempts([3, 1, 2, 3], 4))  # Output: 3
# print(count_rescue_attempts([3, 2, 2, 3], 3))  # Output: 4
# print(count_rescue_attempts([50], 50))  # Output: 1
# print(count_rescue_attempts([5, 5, 5, 5], 15))  # Output: 2
