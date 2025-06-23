from collections import Counter


def longest_palindrome(s: str) -> str:
    freq = Counter(s)

    pairs = []
    center = None

    for char in sorted(freq):
        count = freq[char]
        pairs.extend(char * (count // 2))
        if count % 2 == 1 and center is None:
            center = char

    half = ''.join(pairs)
    if center:
        return half + center + half[::-1]
    else:
        return half + half[::-1]


# print(longest_palindrome('aab'))  # aba
# print(longest_palindrome('qazqaz'))  # aqzzqa
# print(longest_palindrome('abcdef'))  # a
# print(longest_palindrome('a'))  # a
# print(longest_palindrome('bb'))  # bb
# print(longest_palindrome('ccc'))  # ccc
