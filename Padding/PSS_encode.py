from PrimeNumberGeneration.SHA512.SecureHashingAlgorithm import sha_512
from EncryptionDecryption.Seed import seed
from Padding.MaskGenerationFunction import mgf

#function for PSS encoding, takes a message, size of a key in bits, salt length in bytes
def pss_encode(message, em_bits, salt_len = 64):
    m_hash = sha_512(message)
    h_len = 64
    em_len = (em_bits + 7) // 8

    if em_len < h_len + salt_len + 2:
        raise ValueError("Encoding error")

    salt = seed().to_bytes(salt_len, 'big')
    while len(salt) < salt_len:
        salt += sha_512(salt)
    salt = salt[:salt_len]

    m_prime = b'\x00' * 8 + m_hash + salt
    H = sha_512(m_prime)

    ps = b'\x00' * (em_len - salt_len - h_len - 2)
    db = ps + b'\x01' + salt

    db_mask = mgf(H, em_len - h_len - 1)
    masked_db = bytes(x ^ y for x, y in zip(db, db_mask))

    left_bits = 8 * em_len - em_bits
    if left_bits > 0:
        masked_db = bytes([masked_db[0] & (0xFF >> left_bits)]) + masked_db[1:]

    em = masked_db + H + b'\xbc'
    return em
