from SHA256.helpers import shr, rotr, mask


def big_sigma_0(x):
    result = rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
    return result


def big_sigma_1(x):
    result = rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
    return result


def small_sigma_0(x):
    result = rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)
    return result


def small_sigma_1(x):
    result = rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)
    return result

