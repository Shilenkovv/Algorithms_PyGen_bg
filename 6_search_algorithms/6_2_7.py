def add_one(digits):
    """
    Увеличивает число, представленное списком цифр, на единицу.

    Args:
        digits (list): Список, представляющий число, где каждая цифра является отдельным элементом.

    Returns:
        list: Новый список, представляющий увеличенное число.
    """
    n = len(digits)
    carry = 1  # Единица, которую нужно прибавить

    for i in range(n - 1, -1, -1):
        new_digit = digits[i] + carry
        if new_digit == 10:
            digits[i] = 0
            carry = 1
        else:
            digits[i] = new_digit
            carry = 0
            break

    if carry == 1:  # Если остался перенос
        digits.insert(0, 1)

    return digits
