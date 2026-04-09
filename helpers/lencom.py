def comparator(bit_len):
    if bit_len == 512:
        return 40
    elif bit_len >= 1024:
        return 64
    return 0
