#function to calculate modular inverse of a modulo m
def inverse(a, m):
    i = m
    j = a
    y2 = 0
    y1 = 1
    while j > 0:
        quotient = i // j
        remainder = i - j * quotient
        y = y2 - y1 * quotient
        i = j
        j = remainder
        y2 = y1
        y1 = y
    return y2 % m



