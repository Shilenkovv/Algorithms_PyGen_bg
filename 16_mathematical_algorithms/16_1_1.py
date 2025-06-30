def nearest_divisible_by_ten(n: int) -> int:
    dosens = n // 10
    rem = n % 10
    return dosens * 10 if rem <= 4 else (dosens + 1) * 10
