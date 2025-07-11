def is_in_arithmetic(num: int, start: int, step: int) -> bool:
    if num == start:
        return True
    elif (
        (step != 0)
        and ((num - start) % step == 0)
        and ((step > 0 and num > start) or (step < 0 and num < start))
    ):
        return True
    return False


# print(is_in_arithmetic(1, -1, 0))
