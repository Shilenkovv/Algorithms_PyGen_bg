def book_count(prices: list[str], cash: int) -> int:
    n = len(prices)
    if sum(prices) <= cash:
        return n
    tot_spend = 0
    books = 0

    for i in range(n - 1):
        idx = i

        for j in range(i + 1, n):
            if prices[j] <= prices[idx]:
                idx = j
        if i != idx:
            prices[i], prices[idx] = prices[idx], prices[i]
        if cash - tot_spend >= prices[i]:
            tot_spend += prices[i]
            books += 1
        else:
            return books
    return books


# print(book_count([3, 2, 1, 3, 4], 15))  # 5
# print(book_count([3, 2, 1, 3, 4], 8))  # 3
# print(book_count([3], 1))
