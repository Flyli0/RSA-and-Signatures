from Signatures.Hash_and_sign import sign
from Signatures.Hash_and_sign_Verification import verify
from RSA_Key_Generation.KeysGenerator import generate_keys

public, private = generate_keys(1024)

Message = "Cryptography"
Message = Message.encode()
n = public[0]

signature = sign(Message, private, 1024)
print(signature)
signature = signature.to_bytes((n.bit_length()+7)//8,'big')
verificateion = verify(Message, signature, public)
print(verificateion)