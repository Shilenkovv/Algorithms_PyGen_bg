def max_digit(num: int) -> int:
    result = num % 10
    while num > 0:
        digit = num % 10
        if digit > result:
            result = digit
        num //= 10
    return result
