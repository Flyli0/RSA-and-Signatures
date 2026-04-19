def pkcs_unpadding(padded_message):
    if len(padded_message) < 11:
        raise ValueError("Invalid padded message length")

    if padded_message[0] != 0x00 or padded_message[1] != 0x02:
        raise ValueError("Invalid padding format")

    separator_index = padded_message.find(b'\x00', 2)
    if separator_index == -1:
        raise ValueError("Separator not found")

    ps_length = separator_index - 2
    if ps_length < 8:
        raise ValueError("Padding string too short")

    ps = padded_message[2:separator_index]
    if any(byte == 0x00 for byte in ps):
        raise ValueError("Invalid padding: zero byte inside PS")

    message = padded_message[separator_index + 1:]
    return message