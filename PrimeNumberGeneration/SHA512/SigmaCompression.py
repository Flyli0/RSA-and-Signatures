from PrimeNumberGeneration.SHA512.helpers import shr, rotr, mask


def big_sigma_0(x):
    result = rotr(x, 28) ^ rotr(x, 34) ^ rotr(x, 39)
    return result


def big_sigma_1(x):
    result = rotr(x, 14) ^ rotr(x, 18) ^ rotr(x, 41)
    return result


def small_sigma_0(x):
    result = rotr(x, 1) ^ rotr(x, 8) ^ shr(x, 7)
    return result


def small_sigma_1(x):
    result = rotr(x, 19) ^ rotr(x, 61) ^ shr(x, 6)
    return result

