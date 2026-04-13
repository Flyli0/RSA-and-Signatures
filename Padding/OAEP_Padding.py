from helpers.SHA256.SecureHashingAlgorithm import sha_256
from PrimeNumberGeneration.RandomBytes import random_bytes
from Padding.MaskGenerationFunction import mgf
# DB = lHash || PS || 0x01 || message
# EM = 0x00 || ms || mdb


def oaep(bit_len, message, label=""):  # accepts bit length, message and label as text

    byte_len = bit_len//8
    lHash = sha_256(label.encode())
    if len(message) > byte_len - 2 * 32 - 2:  # if message is larger than byte len - hash (space reserved for message)
        raise ValueError("Message too long")

    ps_len = byte_len - (len(message) + 32 + 1)  # length of 0x00 byte string (all except 0x01 separator and 32 byte hash)

    ps = b"\x00"*ps_len  # padding

    seed1 = random_bytes(32)

    DB = lHash + ps + b"\x01" + message  # first part of adding entropy
    dbMask = mgf(seed1,byte_len-32-1)  # mask function exends sha 256 hash till sufficient len
    maskedDb = bytearray(p ^ k for p, k in zip(DB, dbMask))  # our favorite XOR

    seedMask = mgf(maskedDb,32)  # doin same with seed, to ensure its dependence on hash
    maskedSeed = bytearray(p ^ k for p, k in zip(seed1, seedMask))

    EM = b"\x00" + maskedSeed + maskedDb  # encoded "padded" message
    return EM

