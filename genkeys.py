import random

p_value = 0


def is_prime(input_num):
    check_num = input_num
    for divisor in range(2, input_num // 2):
        if (check_num % divisor) == 0:
            check_result = False
            break
        else:
            check_result = True
    return check_result


def generate_random_num():
    while True:
        test_number = random.randint(1, 9999)
        value = None
        value = is_prime(test_number)
        if value:
            break
        else:
            continue
    return test_number


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        return a


if __name__ == '__main__':
    p = generate_random_num()
    print(p)
    q = generate_random_num()
    print(q)

    n = p * q

    # phi is the totient of n
    phi = (p - 1) * (q - 1)

    # choose e between 1, n and relatively prime to phi
    e = random.randrange(1, n)

    g = gcd(e, phi)

    # if not relatively prime, re-generate e
    while g != 1:
        e = random.randrange(1, n)
        g = gcd(e, phi)
