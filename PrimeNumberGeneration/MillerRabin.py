from PrimeNumberGeneration.RandomBytes import random_bytes
from helpers.lencom import comparator


def miller_rabin(bit_size, odd): # Miller Rabin primarity test
    if odd < 2:
        return False
    if odd in (2, 3):
        return True
    if odd % 2 == 0:
        return False
    d = odd - 1  # our odd factor
    s = 0 # power of 2

    while d % 2 == 0: # factoring odd number on 2^s and some odd d
        s+=1
        d//=2

    k = comparator(bit_size) # number of rounds of checking (witnesses)
    for i in range(k):
        a = 2
        rb = random_bytes(bit_size // 8)
        rb = int.from_bytes(rb, "big")
        a = (rb % (odd-3)+2)

        x = pow(a,d,odd) # a^d
        if x == 1 or x == odd - 1:
            continue
        for j in range(s-1):
            x = pow(x,2,odd) # checking a^(dj2) mod odd
            if x == odd-1:
                break
        else:
            return False
    return True

    #print(odd)
    #print(s)
    #print(d)
    #print(d%2==0)
    #print((2**s)*d)
    #print(odd-1 == (2**s)*d)

