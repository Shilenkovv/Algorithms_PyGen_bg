def all_binary_strings(n: int) -> list[str]:
    result = []
    for i in range(2**n):
        # Формируем двоичную строку длины n с ведущими нулями
        binary_str = format(i, '0{}b'.format(n))
        result.append(binary_str)
    return result
