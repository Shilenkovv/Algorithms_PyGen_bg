def filtered_reverse(n: int) -> int:
    ans = 0
    while n > 0:
        cur_dig = n % 10
        if cur_dig != 6 and cur_dig != 9:
            ans = ans * 10 + cur_dig
        n //= 10
    return ans


print(filtered_reverse(26891))
