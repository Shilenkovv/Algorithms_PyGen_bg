def is_in_geometric(num: int, start: int, ratio: int) -> bool:
    while abs(start) <= abs(num):
        if num == start:
            return True
        start *= ratio
    return num == start


# print(is_in_geometric(-24, -3, 2))
