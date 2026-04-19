from Padding.PSS_encode import pss_encode
from Padding.PSS_verify import pss_verify

#PSS encoding, verification test
message = 'fwfe'
message = message.encode()
message = pss_encode(message, 2048, 64)
print(message)

message = 'fwfe'
message = message.encode()
em = pss_encode(message, 2048, 64)

print("Valid:", pss_verify(message, em, 2048, 64))

tampered_message = 'awfe'
tampered_message = tampered_message.encode()

print("Tampered message:", pss_verify(tampered_message, em, 2048, 64))

tampered_em = b'\x00'

print("Tampered signature:", pss_verify(message, tampered_em, 2048, 64))