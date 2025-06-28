def digital_root(n: int) -> int:
    while n > 9:
        sup = n
        ans = 0
        while sup > 0:
            ans += sup % 10
            sup //= 10
        n = ans
    return n


# print(digital_root(9875))  # 2
