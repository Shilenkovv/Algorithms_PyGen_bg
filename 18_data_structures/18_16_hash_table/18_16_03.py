from typing import List


def one_row_words(words: List[str]) -> List[str]:
    first_row_set = set(list('qwertyuiop'))
    second_row_set = set(list('asdfghjkl'))
    third_row_set = set(list('zxcvbnm'))
    ans: List[str] = []

    for word in words:
        if word[0] in first_row_set:
            for syl in word:
                if syl not in first_row_set:
                    break
            else:
                ans.append(word)
        elif word[0] in second_row_set:
            for syl in word:
                if syl not in second_row_set:
                    break
            else:
                ans.append(word)
        elif word[0] in third_row_set:
            for syl in word:
                if syl not in third_row_set:
                    break
            else:
                ans.append(word)
    return ans
