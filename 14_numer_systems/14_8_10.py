def xor_encrypt(message: str, key: str) -> str:
    key_length = len(key)
    encrypted_chars = []
    for i, ch in enumerate(message):
        # Получаем код символа сообщения и соответствующего символа ключа (с циклическим повторением)
        encrypted_char_code = ord(ch) ^ ord(key[i % key_length])
        # Преобразуем обратно в символ и добавляем в результат
        encrypted_chars.append(chr(encrypted_char_code))
    return ''.join(encrypted_chars)
