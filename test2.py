import random, math


n = 77
phi_n = 60

e = random.randrange(1, n)

# check if e and phi_n is relatively prime
g = math.gcd(e, phi_n)

# if not relatively prime, re-generate e
while g != 1:
    e = random.randrange(1, n)
    g = math.gcd(e, phi_n)




print("encrypt key is: ", e)

