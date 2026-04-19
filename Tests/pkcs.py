from Padding.PKCS_Padding import pkcs_padding

message = 'fwfe'
message = message.encode()
pkcs_padding(message,1024)
print(message.decode)