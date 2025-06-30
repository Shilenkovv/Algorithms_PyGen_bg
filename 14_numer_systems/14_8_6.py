def count_reset_bits(num: int) -> int:
    return num.bit_length() - num.bit_count()


print(count_reset_bits(0b1000))
