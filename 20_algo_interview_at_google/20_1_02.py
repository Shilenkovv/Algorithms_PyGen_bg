from typing import List


def count_holidays(birthdays: List[int]) -> int:
    seen: List[bool] = [False] * 32
    for day in birthdays:
        seen[day] = True
    return sum(seen)
