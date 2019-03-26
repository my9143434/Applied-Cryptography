def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        print(a)
        return a


print(gcd(1, 5))

