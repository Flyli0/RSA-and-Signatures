from PrimeNumberGeneration.PrimeGenerator import generate_prime

def generate_keys(bit_size):
    while (True):
        p = generate_prime(bit_size / 2)
        q = generate_prime(bit_size / 2)
        if (abs(p - q) > 2 ** (bit_size / 2 - 100)):
            
