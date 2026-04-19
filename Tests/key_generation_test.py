from RSA_Key_Generation.KeysGenerator import generate_keys

public, private = generate_keys(2048)

print(public)
print(private)