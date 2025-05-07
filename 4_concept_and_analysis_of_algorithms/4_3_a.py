def fizz_buzz(n: int) -> list:
    """Generates a list of numbers from 1 to n with special substitutions:
    - Replaces multiples of 3 with 'Fizz'.
    - Replaces multiples of 5 with 'Buzz'.
    - Replaces multiples of both 3 and 5 with 'FizzBuzz'.

    Args:
        n (int): The upper limit of the range (inclusive), where 1 <= n <= 10^3.

    Returns:
        list: A list of integers and strings, where each integer or substitution corresponds
              to its position in the range [1, n].
    """
    return [
        x if x % 3 and x % 5 else 'Fizz' * (x % 3 == 0) + 'Buzz' * (x % 5 == 0)
        for x in range(1, n + 1)
    ]
