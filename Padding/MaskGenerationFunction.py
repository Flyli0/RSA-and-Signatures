from helpers.SHA256.SecureHashingAlgorithm import sha_256
def mgf(seed,length): # this function extends hash up to required length
    output = b""
    counter = 0
    while(len(output) < length):
        C = counter.to_bytes(4,"big")
        output += sha_256(seed+C)
        counter += 1
    return output[:length]
