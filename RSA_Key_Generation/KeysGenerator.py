from PrimeNumberGeneration.PrimeGenerator import generate_prime
from ModularArithmeticOperations.GCD import gcd

def generate_keys(bit_size):
    while True:
        p = generate_prime(bit_size / 2)
        q = generate_prime(bit_size / 2)
        if abs(p - q) > 2 ** (bit_size / 2 - 100):
            n = p * q
            fi = (p - 1) * (q - 1)
            e = 65537
            if gcd(e, fi) == 1:
                break

    
