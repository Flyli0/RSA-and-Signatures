from PrimeNumberGeneration.RandomBytes import random_bytes
from PrimeNumberGeneration.SHA512.SecureHashingAlgorithm import sha_512


def generate_odd(size_bits):  # using our generator create odds of different size
    size = 0
    size_bytes = size_bits // 8
    sum = 0
    while size < size_bits:
        rnd = random_bytes(size_bytes)
        rnd = sha_512(rnd)
        rnd = int.from_bytes(rnd,"big")
        sum += rnd
        size += 512

    num = sum & ((1 << size_bits) - 1)  # mask to correspond required length
    num = num | (1 << (size_bits - 1))  # MSB first bit must be 1 to ensure required len
    num = num | 1  # LSB last bit must be 1 to ensure oddness of number
    return num  # Integer
