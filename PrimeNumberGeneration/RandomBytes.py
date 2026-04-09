from time import time_ns
from os import getpid

m = 2**64

a = 6364136223846793005

c = 1442695040888963407

# Function that takes byte count to generate and returns pseudo-randomly generated 
# sequence in bytes type


def random_bytes(byte_count):
    # time in nanoseconds since the epoch and process ID are XORed
    pseudo_random_value = time_ns() ^ getpid()
    result = b""
    while len(result) < byte_count:
        pseudo_random_value = (a * pseudo_random_value + c) % m
        result += pseudo_random_value.to_bytes(8, "big")
    return result[:byte_count]

