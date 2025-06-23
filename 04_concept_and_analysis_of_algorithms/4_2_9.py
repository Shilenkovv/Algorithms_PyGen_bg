def min_digit_sum(a: int, b: int) -> int:
    """
    Finds the count of integers in the range [a, b] that have the smallest sum of digits.

    Args:
        a (int): The lower bound of the range (1 ≤ a ≤ 10^6).
        b (int): The upper bound of the range (a ≤ b ≤ 10^6).

    Returns:
        int: The count of numbers with the minimum sum of digits.
    """

    def digit_sum(n: int) -> int:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    min_sum = float('inf')
    count = 0

    for num in range(a, b + 1):
        current_sum = digit_sum(num)
        if current_sum < min_sum:
            min_sum = current_sum
            count = 1
        elif current_sum == min_sum:
            count += 1

    return count
