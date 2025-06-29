def hex_color_code(r: int, g: int, b: int) -> str:
    r_hex = hex(r).replace('0x', '').zfill(2).upper()
    g_hex = hex(g).replace('0x', '').zfill(2).upper()
    b_hex = hex(b).replace('0x', '').zfill(2).upper()

    return '#' + r_hex + g_hex + b_hex
