def adjacent_parity(nums: list[int]) -> bool:
    """
    Determines if the list of integers satisfies specific parity conditions.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        bool: True if the absolute difference between the counts of odd and even numbers
              is at most 1, or if all numbers are either odd or even; otherwise, False.
    """
    odd_count = 0
    even_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (abs(odd_count - even_count) <= 1) or (odd_count == 0) or (even_count == 0)
