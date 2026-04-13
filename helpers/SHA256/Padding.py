def padding(message: bytes) -> bytes:

    if isinstance(message, str):
        message = message.encode()

    original_len = len(message) * 8

    # append 0x80 (bit '1' followed by zeros)
    message += b'\x80'

    # pad zeros until length ≡ 448 (mod 512)
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    # append 64-bit big-endian length
    message += original_len.to_bytes(8, 'big')

    return message
