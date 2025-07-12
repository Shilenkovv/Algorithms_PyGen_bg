def fibonacci(n: int) -> int:
    prev, cur = 1, 1
    for _ in range(n - 2):
        prev, cur = cur, prev + cur
    return cur


def last_digit_of_fibonacci(n: int) -> int:
    return fibonacci(n % 60) % 10


# print(last_digit_of_fibonacci(25))
# print(last_digit_of_fibonacci(85))
# print(last_digit_of_fibonacci(60))
# print(last_digit_of_fibonacci(61))
# print(last_digit_of_fibonacci(120))
