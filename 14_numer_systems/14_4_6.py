from typing import List


def nth_in_nonine_sequence(num: int) -> int:
    ans: List[str] = []

    while num != 0:
        last_digit = num % 9
        ans.append(str(last_digit))
        num //= 9

    return int(''.join(reversed(ans)))


# print(nth_in_nonine_sequence(5))  # 5
# print(nth_in_nonine_sequence(9))  # 10
# print(nth_in_nonine_sequence(13))  # 14
# print(nth_in_nonine_sequence(19))  # 21
