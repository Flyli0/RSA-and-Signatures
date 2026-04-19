# function for RSA encryption
def encrypt(message, public_key):
    n = public_key[0]
    e = public_key[1]
    cipher = pow(message, e, n)
    return cipher