def arabic_to_roman(num: int) -> str:
    # Кортежи с римскими цифрами и их значениями, упорядоченные от больших к меньшим
    val_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    result = ''
    for value, symbol in val_map:
        if num == 0:
            break
        while num >= value:
            result += symbol
            num -= value
    return result


print(arabic_to_roman(15))  # XV
# print(arabic_to_roman(72))  # LXXII
print(arabic_to_roman(149))  # CXLIX
