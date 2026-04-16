from Padding.PKCS_Padding import pkcs_padding
from helpers.SHA256.SecureHashingAlgorithm import sha_256


def sign(message, private_key, bit_size):
    asn1 = bytes.fromhex('3031300d060960864801650304020105000420')
    h = sha_256(message)
    digest_info = asn1 + h
    if len(digest_info) > bit_size//8 - 11:
        raise ValueError("Message too long")

    m = pkcs_padding(digest_info, bit_size)
    n = private_key[0]
    d = private_key[1]
    s = pow(m,d,n)
    return s