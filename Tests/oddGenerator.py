from PrimeNumberGeneration.OddNumberGenerator import generate_odd

a = generate_odd(512)
print(a)
print(a%2 == 0)