from SHA256.SecureHashingAlgorithm import sha_256


def sha_file(path:str):  # function to hash files with sha
    with open(path, "rb") as f:
        data = f.read
    return sha_256(data)


def check(expected_sha, path):  # comparison of an expected file hash and current to check integrity
    current = sha_file(path)
    if current == expected_sha:
        print("File integrity confirmed!")
    else:
        print("File was modified !!!")
