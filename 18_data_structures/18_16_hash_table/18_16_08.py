from collections import Counter


def can_form_palindrome(s: str) -> bool:
    cntr: dict[str, int] = Counter(s)

    one_exc = False

    for k in cntr:
        if cntr[k] % 2 != 0:
            if one_exc:
                return False
            else:
                one_exc = True
    return True
