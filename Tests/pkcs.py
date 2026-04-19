from Padding.PKCS_Padding import pkcs_padding
from Padding.PKCS_Unpadding import pkcs_unpadding

message = 'fwfe'
message = message.encode()

padded = pkcs_padding(message, 1024)
print("Padded:", padded)

recovered = pkcs_unpadding(padded)
print("Recovered:", recovered)

print("Match:", recovered == message)

