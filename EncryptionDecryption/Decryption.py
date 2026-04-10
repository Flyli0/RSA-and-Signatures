def decrypt(cipher, private_key):
    d = private_key[1]
    n = private_key[0]
    message = cipher ** d % n
