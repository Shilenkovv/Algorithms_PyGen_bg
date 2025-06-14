def reverse_vowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']

    cur_vowels = [sym for sym in s if sym in vowels]

    left, right = 0, len(cur_vowels) - 1
    ans = ''
    while left < len(s) or right >= 0:
        if s[left] not in vowels:
            ans += s[left]
        else:
            ans += cur_vowels[right]
            right -= 1
        left += 1

    return ans


# print(reverse_vowels('programmer'))
