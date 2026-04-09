from PrimeNumberGeneration.OddNumberGenerator import generate_odd
from PrimeNumberGeneration.MillerRabin import miller_rabin


def generate_prime(bit_size):
    while True:  # generating random odd number until its prime
        odd = generate_odd(bit_size)
        if miller_rabin(bit_size, odd):  # checking by miller rabin
            return odd


