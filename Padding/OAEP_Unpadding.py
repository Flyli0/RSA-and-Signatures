from MaskGenerationFunction import mgf
from helpers.SHA256.SecureHashingAlgorithm import sha_256

def oaep_unpad(encrypted_message, bit_length, label = ""):
    k = bit_length//8
    em = encrypted_message.to_bytes(k,"big")
    if len(em) != k:
        raise ValueError("Decryption error")
    y = em[0]
    if y != 0:
        raise ValueError("Decryption error")
    maskedSeed = em[1:32+1]
    maskedDb = em[1+32:]
    seedMask = mgf(maskedDb,32)
    seed = bytearray(p ^ k for p, k in zip(maskedSeed, seedMask))
    dbMask = mgf(seed, k-32-1)
    db = bytearray(p^b for p, b in zip(maskedDb, dbMask))

    lHash = sha_256(label.encode)
    lHashPrime = db[:32]

    if lHashPrime != lHash:
        raise ValueError("Decryption error")

    rest = db[32:]

    try:
        ind = rest.index(b"\x01")
    except ValueError:
        raise ValueError("Decryption error")

    PS = rest[:ind]
    if any (b!=0 for b in PS):
        raise ValueError("Decryption error")

    message = rest[ind+1:]

    return message


