def padding(message: bytes) -> bytes:

    original_len = len(message) * 8

    # append 0x80 (bit '1' followed by zeros)
    message += b'\x80'

    while (len(message) + 16) % 128 != 0:
        message += b'\x00'

    message += original_len.to_bytes(16, 'big')

    return message