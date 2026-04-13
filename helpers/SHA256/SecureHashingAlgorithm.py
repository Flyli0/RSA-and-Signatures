from SHA256.Choose import ch
from SHA256.Major import maj
from SHA256.SigmaCompression import small_sigma_0, small_sigma_1, big_sigma_0, big_sigma_1
from SHA256.Padding import padding
from SHA256.Constants import H, K
from SHA256.helpers import mask


def sha_256(message):  # OUR SHA256 realization
    message = padding(message)  # Padding function to make message congruent 512 bits

    Hc = H.copy()  # Copying Initial value array
    Kc = K.copy()

    for i in range(0, len(message), 64):  # Making 512 bit blocks from an entire message (Merkle Damgard construction)
        block = message[i:i + 64]
        W = [0] * 64
        for j in range(16):
            W[j] = int.from_bytes(block[j * 4:(j + 1) * 4], 'big')  # such function for words from 0 to 15

        for j in range(16, 64):
            W[j] = mask(small_sigma_1(W[j - 2]) + W[j - 7] + small_sigma_0(W[j - 15]) + W[j - 16])  # further extension

        a = Hc[0]  # initializing main working variables
        b = Hc[1]
        c = Hc[2]
        d = Hc[3]
        e = Hc[4]
        f = Hc[5]
        g = Hc[6]
        h = Hc[7]

        for t in range(64):  # main cycle of Compression
            T1 = mask(h + big_sigma_1(e) + ch(e, f, g) + Kc[t] + W[t])
            T2 = mask(big_sigma_0(a) + maj(a, b, c))
            h = g
            g = f
            f = e
            e = mask(d + T1)
            d = c
            c = b
            b = a
            a = mask(T1 + T2)

        # Updating hash values
        Hc[0] = mask(Hc[0] + a)
        Hc[1] = mask(Hc[1] + b)
        Hc[2] = mask(Hc[2] + c)
        Hc[3] = mask(Hc[3] + d)
        Hc[4] = mask(Hc[4] + e)
        Hc[5] = mask(Hc[5] + f)
        Hc[6] = mask(Hc[6] + g)
        Hc[7] = mask(Hc[7] + h)
        #  intermediate = b"".join(h.to_bytes(4, 'big') for h in Hc)
        #  print(f"step: {intermediate}")

    digest = b''.join(h.to_bytes(4, 'big') for h in Hc)  # Final concatenation of the results
    return digest
