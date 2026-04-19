from PrimeNumberGeneration.PrimeGenerator import generate_prime
from PrimeNumberGeneration.MillerRabin import miller_rabin


###################TEST1 -> simple primes verification
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_Miller Rabin Test-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
pr = [3,5,7,11,33,12,13,17,31,127]
for p in pr:
    print(p,end=": ")
    if miller_rabin(512, p):
        print("Prime")
    else:
        print("Not Prime")


print("\n\n_-_-_-_-_-_-_-_-_-_-_-_-_-_Prime generator test-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
large_primes_512 = []
large_primes_1024  = []
for i in range(10):
    large_primes_512.append(generate_prime(512))
    large_primes_1024.append(generate_prime(1024))

print("..................512 Primes................")
for p in large_primes_512:
    print(p, end=": ")
    if miller_rabin(512, p):
        print("Prime")
    else:
        print("Not Prime")
print("\n..................1024(or more) Primes................\n")
for p in large_primes_1024:
    print(p, end=": ")
    if miller_rabin(1024, p):
        print("Prime")
    else:
        print("Not Prime")


print("\n\n_-_-_-_-_-_-_-_-_-_-_-_-_-_Carmichael numbers-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
cmNum = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101,
         115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065,
         488881, 512461, 530881, 552721]  # first several known (it's a Composite numbers, but they have lots of relatively prime integers, and look like primes)

for p in cmNum:
    print(p, end=": ")
    if miller_rabin(512, p):
        print("Prime")
    else:
        print("Not Prime")





        