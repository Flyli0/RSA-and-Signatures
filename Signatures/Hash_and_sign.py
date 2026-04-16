from EncryptionDecryption.Encryption import encrypt
from Padding.PKCS_Padding import pkcs_padding


def sign(message, private_key, bit_size):
    m = pkcs_padding(message, bit_size)
    n = private_key[0]
    d = private_key[1]
    s = pow(m,d,n)
    return s