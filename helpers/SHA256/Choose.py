def ch(x, y, z):
    not_x = (~x) & 0xFFFFFFFF  # masking to prevent negative numbers
    check = (x & y) ^ (not_x & z)
    return check
