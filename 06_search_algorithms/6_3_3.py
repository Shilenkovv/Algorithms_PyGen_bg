def golden_pairs(pairs: list[tuple]):
    ans = 0
    for pair in pairs:
        if pair[0] == pair[1]:
            continue
        else:
            if 1.6 <= max(pair) / min(pair) <= 1.7:
                ans += 1
    return ans
