from PrimeNumberGeneration.SHA512.SecureHashingAlgorithm import sha_512
from Padding.MaskGenerationFunction import mgf

#function for PSS verification, takes message, encoded message, its size in bits, salt length in
# bytes
def pss_verify(message, em, em_bits, salt_len=64):
    m_hash = sha_512(message)
    h_len = 64
    em_len = (em_bits + 7) // 8

    if em_len < h_len + salt_len + 2:
        return False

    if em[-1] != 0xbc:
        return False

    masked_db = em[:em_len - h_len - 1]
    H = em[em_len - h_len - 1:em_len - 1]

    left_bits = 8 * em_len - em_bits
    if left_bits > 0:
        if masked_db[0] >> (8 - left_bits) != 0:
            return False

    db_mask = mgf(H, em_len - h_len - 1)
    db = bytes(x ^ y for x, y in zip(masked_db, db_mask))

    if left_bits > 0:
        db = bytes([db[0] & (0xFF >> left_bits)]) + db[1:]

    ps_len = em_len - h_len - salt_len - 2
    if db[:ps_len] != b'\x00' * ps_len:
        return False

    if db[ps_len] != 0x01:
        return False

    salt = db[-salt_len:]

    m_prime = b'\x00' * 8 + m_hash + salt
    H_check = sha_512(m_prime)

    return H == H_check