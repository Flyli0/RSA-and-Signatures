from PrimeNumberGeneration.SHA512.SecureHashingAlgorithm import sha_512
from EncryptionDecryption.Seed import seed

#function for PKCS padding, takes message and size of key in bits
def pkcs_padding(message, bit_size):
    byte_size = bit_size // 8
    ps_length = byte_size - (3 + len(message))
    ps = b""
    raw_bytes = seed()
    while len(ps) < ps_length:
        raw_bytes = sha_512(raw_bytes)
        non_zero_bytes = bytes(byte for byte in raw_bytes if byte != 0)
        ps += non_zero_bytes
    padded_message = b'\x00\x02' + ps + b'\x00' + message
    return padded_message