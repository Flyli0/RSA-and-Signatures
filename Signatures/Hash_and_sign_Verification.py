from EncryptionDecryption.Decryption import decrypt
from helpers.SHA256.SecureHashingAlgorithm import sha_256


def verify(message, signature, public_key):
    n = public_key[0]
    e = public_key[1]
    if isinstance(signature, bytes):
        s = int.from_bytes(signature,'big')
    else:
        s = signature
    m = pow(s, e, n)
    k = (n.bit_length() + 7) // 8
    EM = m.to_bytes(k, "big")

    if EM[0] != 0x00 or EM[1] != 0x01:  # checking structure
        return False

    try:
        sep_index = EM.index(b"\x00", 2)
    except ValueError:
        return False

    PS = EM[2:sep_index]

    if len(PS) < 8 or any(b != 0xFF for b in PS):
        return False

    digest_info = EM[sep_index+1:]
    asn = bytes.fromhex("3031300d060960864801650304020105000420")
    expected_hash = sha_256(message)
    expected_info = asn+expected_hash
    return expected_info == digest_info
