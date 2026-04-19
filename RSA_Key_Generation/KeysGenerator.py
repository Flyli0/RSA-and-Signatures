from PrimeNumberGeneration.PrimeGenerator import generate_prime
from ModularArithmeticOperations.GCD import gcd
from ModularArithmeticOperations.ExtendedEuclideanAlgorithm import inverse

def generate_keys(bit_size):
    while True:
        p = generate_prime(bit_size // 2)
        q = generate_prime(bit_size // 2)
        if abs(p - q) > 2 ** (100):  # (bit_size / 2 - 100)
            n = p * q
            fi = (p - 1) * (q - 1)
            e = 65537
            if gcd(e, fi) == 1:
                break
    d = inverse(e, fi)

    dP = d % (p-1)  # shortened powers by Fermat little theorem's corollary for CRT optimization
    dQ = d % (q-1)
    qInv = inverse(q,p)  # inverse of q modulo p is needed to compute h (corrector for m2 to match mod pq)
    print(e * d % fi == 1)
    public_key = (n, e)
    private_key = (n, d, p, q, dP, dQ, qInv)
    return public_key, private_key

