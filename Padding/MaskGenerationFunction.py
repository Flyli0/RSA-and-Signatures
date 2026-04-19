from helpers.SHA256.SecureHashingAlgorithm import sha_256
def mgf(seed, length):
    output = bytearray()
    counter = 0

    while len(output) < length:
        C = counter.to_bytes(4, "big")

        digest = sha_256(seed + C)

        if isinstance(digest, str):
            digest = bytes.fromhex(digest)
        elif isinstance(digest, int):
            digest = digest.to_bytes(32, "big")

        output.extend(digest)
        counter += 1
        # print(length)
    return bytes(output[:length])
