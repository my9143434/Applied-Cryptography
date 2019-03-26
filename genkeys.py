import random, math

p_value = 0


def is_prime(input_num):
    check_num = input_num
    check_result = None
    for divisor in range(2, input_num // 2):
        if (check_num % divisor) == 0:
            check_result = False
            break
        else:
            check_result = True
    return check_result


def generate_random_num():
    while True:
        test_number = random.randint(1, 1000)
        value = None
        value = is_prime(test_number)
        if value:
            break
        else:
            continue
    return test_number


def modular_inverse(input_e, input_phi_n):
    temp_remainder = 0
    test_d = 0
    while temp_remainder != 1:
        test_d += 1
        temp_remainder = (input_e * test_d) % input_phi_n

    return test_d


if __name__ == '__main__':
    p = generate_random_num()
    print("p is :", p)
    q = generate_random_num()
    print("q is :", q)

    n = p * q

    # phi is the totient of n
    phi_n = (p - 1) * (q - 1)
    print("phi_n is :", phi_n)

    # choose e between 1, n and relatively prime to phi
    print("finding e")
    e = random.randrange(1, n)

    # check if e and phi_n is relatively prime
    g = math.gcd(e, phi_n)

    # if not relatively prime, re-generate e
    while g != 1:
        e = random.randrange(1, n)
        # print(e)
        g = math.gcd(e, phi_n)

    print("encrypt key is: ", e)

    print("finding d:")
    d = modular_inverse(e, phi_n)
    print("decryption number  is: ", d)
