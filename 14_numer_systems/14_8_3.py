def reset_last_k_bits(num: int, k: int) -> int:
    return num >> k << k
