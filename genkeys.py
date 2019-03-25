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


def modular_inverse(input_e, input_phi_n):
    temp_remainder = 0
    test_d = 0
    while temp_remainder != 1:
        test_d += 1
        print(test_d)
        temp_remainder = (input_e * test_d) % input_phi_n

    return test_d


if __name__ == '__main__':
    p = generate_random_num()
    print(p)
    q = generate_random_num()
    print(q)

    n = p * q

    # phi is the totient of n
    phi_n = (p - 1) * (q - 1)

    # choose e between 1, n and relatively prime to phi
    e = random.randrange(1, n)

    # check if e and phi_n is relatively prime
    g = gcd(e, phi_n)

    # if not relatively prime, re-generate e
    while g != 1:
        e = random.randrange(1, n)
        print(e)
        g = gcd(e, phi_n)

    print(g)

    d = modular_inverse(e, phi_n)
    print(d)
