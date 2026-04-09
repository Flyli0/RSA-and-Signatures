def ch(x, y, z):
    not_x = (~x) & 0xffffffffffffffff # masking to prevent negative numbers
    check = (x & y) ^ (not_x & z)
    return check
