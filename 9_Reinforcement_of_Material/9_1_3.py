def max_profit(prices: list[int], k: int) -> int:
    prices.sort()
    return abs(sum(filter(lambda x: x < 0, prices[:k])))


# print(max_profit([1, -2, -3, -4, 5], 10))
