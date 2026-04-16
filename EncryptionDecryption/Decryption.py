def decrypt(cipher, private_key):
    n, d, p, q, dP, dQ, qInv = private_key

    m1 = pow(cipher, dP, p)  # computing crt arguments m1, m2 (relatively prime numbers)
    m2 = pow(cipher, dQ, q)

    h = (qInv * (m1-m2))%p  # calculating correction
    message = m2 + h * q  # we used m2 as base and just added some k*q, so it satisfies x = p mod m1 and x = 1 mod m2
    return message
