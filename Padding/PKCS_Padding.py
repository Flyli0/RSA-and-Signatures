from PrimeNumberGeneration.RandomBytes import random_bytes

#function that takes message and padded_message length in bytes and returns padded message
def pkcs_padding(message, k):
    m_len = len(message)

    if m_len > k - 11:
        raise ValueError("Message too long")

    ps_len = k - m_len - 3

    ps = bytearray()
    while len(ps) < ps_len:
        chunk = random_bytes(ps_len - len(ps))
        for b in chunk:
            if b != 0:
                ps.append(b)
                if len(ps) == ps_len:
                    break

    return b'\x00\x02' + bytes(ps) + b'\x00' + message