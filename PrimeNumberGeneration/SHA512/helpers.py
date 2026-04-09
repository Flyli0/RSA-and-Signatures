def mask(*args):
    return sum(args) & 0xffffffffffffffff


def rotr(x, n):  # cyclic right shift
    return mask(((x >> n) | (x << (64 - n))))  # standard shift to right and concatenation with right n bits


def shr(x, n):  # right shift
    return x >> n
