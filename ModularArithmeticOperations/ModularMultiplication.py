def square_and_multiply(base,exponent,modulus):
    result = 1
    base = base % modulus
    while exponent>0:
        if exponent%2!=0:
            result = (result * base)%modulus
        exponent = exponent >> 1
        base = (base * base)%modulus
    return result
