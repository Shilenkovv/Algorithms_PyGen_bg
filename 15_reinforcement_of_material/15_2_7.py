def leave_last_k_bits(num: int, k: int) -> int:
    mask = (1 << k) - 1  # Создаём маску с k младшими битами
    return num & mask  # Применяем маску через побитовое И
