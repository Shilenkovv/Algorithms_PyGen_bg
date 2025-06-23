def are_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    char_count = [0] * 26

    for char in s1:
        char_count[ord(char) - ord('a')] += 1

    for char in s2:
        char_count[ord(char) - ord('a')] -= 1
        if char_count[ord(char) - ord('a')] < 0:
            return False

    return True
