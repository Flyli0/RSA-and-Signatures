from EncryptionDecryption.Decryption import decrypt
from EncryptionDecryption.Encryption import encrypt
from RSA_Key_Generation.KeysGenerator import generate_keys
from Padding.OAEP_Padding import oaep
from Padding.OAEP_Unpadding import oaep_unpad


public, private = generate_keys(1024)

Message = "Cryptography"
Message = Message.encode()

# 1. padding
EM = oaep(1024, Message)

# 2. bytes → int
m_int = int.from_bytes(EM, "big")

# 3. encrypt
c = encrypt(m_int, public)
print(c)

# 4. decrypt
m = decrypt(c, private)

# 5. int → bytes
k = (private[0].bit_length() + 7) // 8
EM = m.to_bytes(k, "big")

# 6. unpad
msg = oaep_unpad(m, 1024)   # если твоя функция ждёт int
# или:
# msg = oaep_unpad(EM, 1024)  # если bytes
print(msg)
print(msg.decode())
