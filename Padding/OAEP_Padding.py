from helpers.SHA256.SecureHashingAlgorithm import sha_256
from PrimeNumberGeneration.RandomBytes import random_bytes
from Padding.MaskGenerationFunction import mgf
# DB = lHash || PS || 0x01 || message
# EM = 0x00 || ms || mdb


def oaep(bit_len, message, label=""):  # accepts bit length, message and label as text

    byte_len = bit_len//8
    hLen = 32
    k = byte_len
    lHash = sha_256(label.encode())
    if len(message) > byte_len - 2 * hLen - 2:  # if message is larger than byte len - hash (space reserved for message)
        raise ValueError("Message too long")

    ps_len = k - len(message) - hLen*2 - 2  # length of 0x00 byte string (all except 0x01 separator and 32 byte hash)

    ps = b"\x00"*ps_len  # padding

    seed1 = random_bytes(hLen)

    DB = lHash + ps + b"\x01" + message  # first part of adding entropy
    if len(DB) != k - hLen - 1:
        raise ValueError("DB length mismatch")
    dbMask = mgf(seed1,k-hLen-1)  # mask function exends sha 256 hash till sufficient len
    maskedDb = bytes(DB[i] ^ dbMask[i] for i in range(len(DB)))  # our favorite XOR

    seedMask = mgf(maskedDb,hLen)  # doin same with seed, to ensure its dependence on hash
    maskedSeed = bytes(seed1[i] ^ seedMask[i] for i in range(len(seed1)))

    EM = b"\x00" + maskedSeed + maskedDb  # encoded "padded" message
    return EM

