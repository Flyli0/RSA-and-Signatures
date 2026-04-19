from Padding.MaskGenerationFunction import mgf
from helpers.SHA256.SecureHashingAlgorithm import sha_256

def oaep_unpad(encrypted_message, bit_length, label = ""):
    k = bit_length//8
    hLen = 32
    em = encrypted_message#.to_bytes(k,"big")
    if len(em) != k:
        raise ValueError("Decryption error")
    y = em[0]
    if y != 0:
        raise ValueError("Decryption error")
    maskedSeed = em[1:hLen+1]
    maskedDb = em[1+hLen:]
    seedMask = mgf(maskedDb,hLen)
    seed = bytes(maskedSeed[i] ^ seedMask[i] for i in range(len(maskedSeed)))
    dbMask = mgf(seed, k-hLen-1)
    db = bytes(maskedDb[i] ^ dbMask[i] for i in range(len(maskedDb)))

    lHash = sha_256(label.encode() if isinstance(label, str) else label)
    lHashPrime = db[:hLen]

    if lHashPrime != lHash:
        raise ValueError("Decryption error")

    rest = db[hLen:]

    try:
        ind = rest.index(b"\x01")
    except ValueError:
        raise ValueError("Decryption error")

    PS = rest[:ind]
    if any (b!=0 for b in PS):
        raise ValueError("Decryption error")

    message = rest[ind+1:]

    return message



