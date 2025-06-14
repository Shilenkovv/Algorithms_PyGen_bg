def is_almost_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    bad_sym_found = False

    while left < right:
        if s[left] != s[right]:
            if bad_sym_found:
                return False
            elif s[left + 1] == s[right]:
                bad_sym_found = True
                left += 1
            elif s[left] == s[right - 1]:
                bad_sym_found = True
                right -= 1
            else:
                return False
        else:
            left += 1
            right -= 1

    return True


# print(is_almost_palindrome('abca'))  # aba - True
# print(is_almost_palindrome('abcddba'))  # abddba - True
# print(is_almost_palindrome('spyder'))  # False
# print(is_almost_palindrome('a'))  # True
# print(is_almost_palindrome('aaa'))  # True
