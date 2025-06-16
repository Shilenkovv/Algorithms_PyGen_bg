def smallest_palindrome(s: str) -> str:
    left, right = 0, len(s) - 1
    ans = ''

    while left < right:
        if s[left] >= s[right]:
            ans += s[right]
        elif s[left] < s[right]:
            ans += s[left]
        left += 1
        right -= 1
    # if len(s) % 2:
    #     ans += s[len(s) // 2]
    return ans + len(s) % 2 * s[len(s) // 2] + ans[::-1]


# print(smallest_palindrome('beegeek')) # beegeeb
